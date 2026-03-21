import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# =============================================================================
# Hantek_DPO8054E — Осциллограф (Hantek)
# =============================================================================

# Присвоение имени драйвера
OSC = "Hantek_DPO8054E"

# --- Инициализация и сброс ---------------------------------------------------
MOKO.Driver(OSC, "set", "*RST")                    # Сброс
MOKO.Driver(OSC, "set", "*CLS")                    # Очистка ошибок
idn = MOKO.Driver(OSC, "get", "*IDN?")             # Идентификация

# --- Настройка канала --------------------------------------------------------
MOKO.Driver(OSC, "set", "channel = 1")             # Выбор канала 1
MOKO.Driver(OSC, "set", "channel_state = ON")      # Включение канала
MOKO.Driver(OSC, "set", "SCPI = CHAN1:STAT ON")    # Прямая SCPI

MOKO.Driver(OSC, "set", "vertical_scale = 0.1")    # Вертикальная шкала 100 мВ/дел
MOKO.Driver(OSC, "set", "SCPI = CHAN1:SCAL 0.1")   # Прямая SCPI

MOKO.Driver(OSC, "set", "vertical_offset = 0")     # Смещение по вертикали
MOKO.Driver(OSC, "set", "SCPI = CHAN1:OFFS 0")     # Прямая SCPI

# --- Настройка развёртки -----------------------------------------------------
MOKO.Driver(OSC, "set", "time_scale = 0.0002")     # 200 мкс/дел
MOKO.Driver(OSC, "set", "SCPI = TIM:SCAL 200US")   # Прямая SCPI

# --- Настройка триггера ------------------------------------------------------
MOKO.Driver(OSC, "set", "trigger_type = EDGE")     # Тип триггера: по фронту
MOKO.Driver(OSC, "set", "SCPI = TRIG:TYPE EDGE")   # Прямая SCPI

MOKO.Driver(OSC, "set", "trigger_source = CHAN1")  # Источник триггера
MOKO.Driver(OSC, "set", "SCPI = TRIG:SOUR CHAN1")  # Прямая SCPI

MOKO.Driver(OSC, "set", "trigger_level = 0.05")    # Уровень триггера 50 мВ
MOKO.Driver(OSC, "set", "SCPI = TRIG:LEV 0.05")    # Прямая SCPI

# --- Режим усреднения --------------------------------------------------------
MOKO.Driver(OSC, "set", "averages = 16")           # Количество усреднений 16
MOKO.Driver(OSC, "set", "SCPI = ACQ:AVER:COUN 16") # Прямая SCPI

MOKO.Driver(OSC, "set", "acquire_run")             # Запуск сбора данных
MOKO.Driver(OSC, "set", "SCPI = ACQ:STAT RUN")     # Прямая SCPI

# --- Получение данных --------------------------------------------------------
MOKO.Driver(OSC, "set", "*OPC?")                   # Ожидание готовности

waveform = MOKO.Driver(OSC, "get", "waveform")     # Получение осциллограммы
waveform = MOKO.Driver(OSC, "get", "SCPI = CHAN1:DATA?")  # Прямая SCPI

# --- Автоматические измерения -------------------------------------------------
pulse_width = MOKO.Driver(OSC, "get", "pulse_width")  # Длительность импульса
pulse_width = MOKO.Driver(OSC, "get", "SCPI = MEAS:PULS:WID?")  # Прямая SCPI

rise_time = MOKO.Driver(OSC, "get", "rise_time")   # Время нарастания
rise_time = MOKO.Driver(OSC, "get", "SCPI = MEAS:PULS:RISE?")  # Прямая SCPI

fall_time = MOKO.Driver(OSC, "get", "fall_time")   # Время спада
fall_time = MOKO.Driver(OSC, "get", "SCPI = MEAS:PULS:FALL?")  # Прямая SCPI

amplitude = MOKO.Driver(OSC, "get", "amplitude")   # Амплитуда
amplitude = MOKO.Driver(OSC, "get", "SCPI = MEAS:AMPL?")  # Прямая SCPI

frequency = MOKO.Driver(OSC, "get", "frequency")   # Частота
frequency = MOKO.Driver(OSC, "get", "SCPI = MEAS:FREQ?")  # Прямая SCPI