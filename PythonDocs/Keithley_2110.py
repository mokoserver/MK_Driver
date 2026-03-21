import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# =============================================================================
# Keithley_2110 — Прецизионный мультиметр (Keithley / Tektronix)
# Аналог для Hantek_HDM3075
# Подключение: USB-VISA
# =============================================================================

# Присвоение имени драйвера
DMM = "Keithley_2110"

# --- Инициализация и сброс ---------------------------------------------------
MOKO.Driver(DMM, "set", "*RST")                      # Сброс
MOKO.Driver(DMM, "set", "*CLS")                      # Очистка ошибок
idn = MOKO.Driver(DMM, "get", "*IDN?")               # Идентификация

# --- Конфигурация измерения тока ---------------------------------------------
MOKO.Driver(DMM, "set", "function = DCI")            # Режим: измерение постоянного тока
MOKO.Driver(DMM, "set", "range = 1.0")               # Предел измерения 1 А
MOKO.Driver(DMM, "set", "SCPI = CONF:CURR:DC 1")     # Прямая SCPI (Keithley синтаксис)

MOKO.Driver(DMM, "set", "rate = SLOW")               # Режим: медленный (6½ разрядов)
MOKO.Driver(DMM, "set", "SCPI = CURR:DC:NPLC 10")    # Прямая SCPI (Keithley: 10 PLC = медленно)

MOKO.Driver(DMM, "set", "samples = 10")              # Количество отсчётов для усреднения
MOKO.Driver(DMM, "set", "SCPI = SAMP:COUN 10")       # Прямая SCPI

MOKO.Driver(DMM, "set", "average = ON")              # Включение расчёта среднего
MOKO.Driver(DMM, "set", "SCPI = CALC:FUNC MEAN")     # Прямая SCPI

# --- Получение измерений -----------------------------------------------------
current = MOKO.Driver(DMM, "get", "read")            # Считывание усреднённого тока
current = MOKO.Driver(DMM, "get", "SCPI = READ?")    # Прямая SCPI

current_fast = MOKO.Driver(DMM, "get", "measure_current")  # Быстрое измерение
current_fast = MOKO.Driver(DMM, "get", "SCPI = MEAS:CURR:DC?")  # Прямая SCPI

# --- Проверка ошибок ---------------------------------------------------------
error = MOKO.Driver(DMM, "get", "SCPI = SYST:ERR?")  # Чтение ошибки