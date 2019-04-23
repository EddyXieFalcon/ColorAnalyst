# coding=utf-8

# 硬件指令表

DeviceInstructionsMap = {
    "shake": "hsk\\n",  # 通信握手
    "status": "sta\\n",  # 检测设备状态
    "set_id": "set id=%s\\n",  # 通讯ID设置
    "set_cww": "set cww=%s\\n",  # 电机运行方向设
    "set_spd": "set spd=%s\\n",  # 速度设置
    "set_sds": "set sds=%s\\n",  # 启动速度设置
    "set_sde": "set sde=%s\\n",  # 停止速度设置
    "set_acc": "set acc=%s\\n",  # 加速度设置
    "set_dec": "set dec=%s\\n",  # 减速度设置
    "set_crn": "set crn=%s\\n",  # 匀速电流设置
    "set_crh": "set crh=%s\\n",  # 保持电流设置
    "set_sdr": "set sdr=%s\\n",  # 传感器1触发动作
    "set_stl": "set stl=%s\\n",  # 传感器1触发（遮挡）时时电平设置
    "set_ssdr": "set ssdr=%s\\n",  # 传感器2触发动作
    "set_sstl": "set sstl=%s\\n",  # 传感器2触发（遮挡）时时电平设置
    "set_rsd": "set rsd=%s\\n",  # 复位速度设置
    "set_rsp": "set rsp=%s\\n",  # 复位后安全位置设置
    "set_arm": "set arm=%s\\n",  # 自动运行模式设置
    "set_art": "set art=%s\\n",  # 自动运行倒计时设
}