# -- coding: utf-8 --

import sys
import msvcrt

from ctypes import *

from SoftWare.ThirdParty.MVS.MvImport.MvCameraControl_header import *
from SoftWare.ThirdParty.MVS.MvImport.CameraParams_const import *

if __name__ == "__main__":
    # 设备信息列表的数据结构体
    deviceList = MV_CC_DEVICE_INFO_LIST()
    # 设置设备数据线接口类型（通信规范）
    tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE

    # ch:枚举设备 | en:Enum device —— 查询
    ret = MvCamera.MV_CC_EnumDevices(tlayerType, deviceList)

    # 容错，没有查到设备类型
    if ret != 0:
        print("enum devices fail! ret[0x%x]" % ret)
        sys.exit()

    # 如果设备数量为0
    if deviceList.nDeviceNum == 0:
        print("find no device!")
        sys.exit()

    # 打印，输出设备数量
    print("find %d devices!" % deviceList.nDeviceNum)

    # 轮询每一个设备
    for i in range(0, deviceList.nDeviceNum):
        # 抓取每一个设备的具体信息数据
        mvcc_dev_info = cast(deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
        # 判断设备类型，如果是GIGE设备
        if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE:
            print("\ngige device: [%d]" % i)
            # 准备数据容器
            strModeName = ""
            # 将获取的设备信息进行解析，并放入容器，然后打印
            for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName:
                strModeName = strModeName + chr(per)
            print("device model name: %s" % strModeName)

            # 解析GIGE设备IP地址
            nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
            nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
            nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
            nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
            print("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))
        # 判断设备类型，如果是USB设备
        elif mvcc_dev_info.nTLayerType == MV_USB_DEVICE:
            print("\nu3v device: [%d]" % i)
            # 准备数据容器（工作模式）
            strModeName = ""
            # 解析设备信息，并打印
            for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chModelName:
                if per == 0:
                    break
                strModeName = strModeName + chr(per)
            print("device model name: %s" % strModeName)

            # 准备数据容器（串口信息）
            strSerialNumber = ""
            # 解析设备信息，并打印
            for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chSerialNumber:
                if per == 0:
                    break
                strSerialNumber = strSerialNumber + chr(per)
            print("user serial number: %s" % strSerialNumber)

    # 输入需要连接那个设备
    nConnectionNum = input("please input the number of the device to connect:")

    # 容错，防止非法输入
    if int(nConnectionNum) >= deviceList.nDeviceNum:
        print("intput error!")
        sys.exit()

    # ch:创建相机实例 | en:Creat Camera Object
    cam = MvCamera()

    # ch:选择设备并创建句柄 | en:Select device and create handle
    stDeviceList = cast(deviceList.pDeviceInfo[int(nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents

    # 创建设备连接句柄
    ret = cam.MV_CC_CreateHandle(stDeviceList)
    if ret != 0:
        print("create handle fail! ret[0x%x]" % ret)
        sys.exit()

    # ch:打开设备 | en:Open device
    ret = cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
    if ret != 0:
        print("open device fail! ret[0x%x]" % ret)
        sys.exit()

    # ch:探测网络最佳包大小(只对GigE相机有效) | en:Detection network optimal package size(It only works for the GigE camera)
    if stDeviceList.nTLayerType == MV_GIGE_DEVICE:
        nPacketSize = cam.MV_CC_GetOptimalPacketSize()
        if int(nPacketSize) > 0:
            ret = cam.MV_CC_SetIntValue("GevSCPSPacketSize", nPacketSize)
            if ret != 0:
                print("Warning: Set Packet Size fail! ret[0x%x]" % ret)
        else:
            print("Warning: Get Packet Size fail! ret[0x%x]" % nPacketSize)

    # ch:设置触发模式为off | en:Set trigger mode as off
    ret = cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF)
    if ret != 0:
        print("set trigger mode fail! ret[0x%x]" % ret)
        sys.exit()

    # ch:获取数据包大小 | en:Get payload size
    stParam = MVCC_INTVALUE()
    memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

    # 获取Integer型属性值
    ret = cam.MV_CC_GetIntValue("PayloadSize", stParam)
    if ret != 0:
        print("get payload size fail! ret[0x%x]" % ret)
        sys.exit()
    nPayloadSize = stParam.nCurValue

    # ch:开始取流 | en:Start grab image
    ret = cam.MV_CC_StartGrabbing()
    if ret != 0:
        print("start grabbing fail! ret[0x%x]" % ret)
        sys.exit()

    # 创建设备信息列表数据结构体
    stDeviceList = MV_FRAME_OUT_INFO_EX()
    # 为上述数据结构体填装数据
    memset(byref(stDeviceList), 0, sizeof(stDeviceList))
    # 创建数据缓冲区
    data_buf = (c_ubyte * nPayloadSize)()

    # 定时抓取数据
    ret = cam.MV_CC_GetOneFrameTimeout(byref(data_buf), nPayloadSize, stDeviceList, 1000)
    # 判断是否获取成功
    if ret == 0:
        # 打印抓取的帧
        print("get one frame: Width[%d], Height[%d], nFrameNum[%d]" % (
            stDeviceList.nWidth, stDeviceList.nHeight, stDeviceList.nFrameNum))

        # 解析数据
        nRGBSize = stDeviceList.nWidth * stDeviceList.nHeight * 3
        stConvertParam = MV_CC_PIXEL_CONVERT_PARAM()
        memset(byref(stConvertParam), 0, sizeof(stConvertParam))
        stConvertParam.nWidth = stDeviceList.nWidth
        stConvertParam.nHeight = stDeviceList.nHeight
        stConvertParam.pSrcData = data_buf
        stConvertParam.nSrcDataLen = stDeviceList.nFrameLen
        stConvertParam.enSrcPixelType = stDeviceList.enPixelType
        stConvertParam.enDstPixelType = PixelType_Gvsp_RGB8_Packed
        stConvertParam.pDstBuffer = (c_ubyte * nRGBSize)()
        stConvertParam.nDstBufferSize = nRGBSize

        # 进行数据类型转换
        ret = cam.MV_CC_ConvertPixelType(stConvertParam)
        if ret != 0:
            print("convert pixel fail! ret[0x%x]" % ret)
            del data_buf
            sys.exit()

        # 设置文件路径
        file_path = "AfterConvert_RGB.raw"
        # 打开文件
        file_open = open(file_path.encode('ascii'), 'wb+')
        # 数据保存
        try:
            img_buff = (c_ubyte * stConvertParam.nDstLen)()
            cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen)
            file_open.write(img_buff)
        except:
            raise Exception("save file executed failed:%s" % e.message)
        finally:
            file_open.close()
    else:
        print("get one frame fail, ret[0x%x]" % ret)

    print("convert pixeltype succeed!")

    print("press a key to continue.")
    # 阻塞，等待键盘任意按键按下
    msvcrt.getch()

    # ch:停止取流 | en:Stop grab image
    ret = cam.MV_CC_StopGrabbing()
    if ret != 0:
        print("stop grabbing fail! ret[0x%x]" % ret)
        del data_buf
        sys.exit()

    # ch:关闭设备 | Close device
    ret = cam.MV_CC_CloseDevice()
    if ret != 0:
        print("close deivce fail! ret[0x%x]" % ret)
        del data_buf
        sys.exit()

    # ch:销毁句柄 | Destroy handle
    ret = cam.MV_CC_DestroyHandle()
    if ret != 0:
        print("destroy handle fail! ret[0x%x]" % ret)
        del data_buf
        sys.exit()

    # 删除数据缓冲
    del data_buf
