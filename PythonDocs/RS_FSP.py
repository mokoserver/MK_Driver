import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# =============================================================================
# RS_FSV30 — Анализатор спектра (Rohde & Schwarz)
# Аналог для Ceyear_RSA4082
# IP: 169.254.1.123
# =============================================================================

# Присвоение имени драйвера
SA = "RS_FSV30"

# --- Инициализация и сброс ---------------------------------------------------
MOKO.Driver(SA, "set", "*RST")                         # Сброс
MOKO.Driver(SA, "set", "*CLS")                         # Очистка ошибок
idn = MOKO.Driver(SA, "get", "*IDN?")                  # Идентификация

# --- Настройка частоты ------------------------------------------------------
MOKO.Driver(SA, "set", "center_frequency = 2400000000")    # Центральная частота 2.4 ГГц
MOKO.Driver(SA, "set", "SCPI = FREQ:CENT 2.4GHZ")         # Прямая SCPI

MOKO.Driver(SA, "set", "span = 100000000")             # Полоса обзора 100 МГц
MOKO.Driver(SA, "set", "SCPI = FREQ:SPAN 100MHZ")      # Прямая SCPI

# --- Настройка полос фильтров ------------------------------------------------
MOKO.Driver(SA, "set", "rbw = 100000")                 # RBW = 100 кГц
MOKO.Driver(SA, "set", "SCPI = BAND:RES 100KHZ")       # Прямая SCPI

MOKO.Driver(SA, "set", "vbw = 10000")                  # VBW = 10 кГц
MOKO.Driver(SA, "set", "SCPI = BAND:VID 10KHZ")        # Прямая SCPI

# --- Детектор и усреднение ---------------------------------------------------
MOKO.Driver(SA, "set", "detector = PEAK")              # Пиковый детектор
MOKO.Driver(SA, "set", "SCPI = DET:FUNC PEAK")         # Прямая SCPI

MOKO.Driver(SA, "set", "averages = 10")                # Количество усреднений 10
MOKO.Driver(SA, "set", "SCPI = AVER:COUN 10")          # Прямая SCPI

# --- Запуск измерения и получение данных ------------------------------------
MOKO.Driver(SA, "set", "initiate")                     # Запуск сканирования
MOKO.Driver(SA, "set", "SCPI = INIT:IMM")              # Прямая SCPI

MOKO.Driver(SA, "set", "*OPC?")                        # Ожидание завершения

trace = MOKO.Driver(SA, "get", "trace")                # Получение спектра
trace = MOKO.Driver(SA, "get", "SCPI = TRAC:DATA? TRACE1")  # Прямая SCPI

# --- Маркеры -----------------------------------------------------------------
MOKO.Driver(SA, "set", "marker_max")                   # Маркер на максимум
MOKO.Driver(SA, "set", "SCPI = CALC:MARK:MAX")         # Прямая SCPI

peak_freq = MOKO.Driver(SA, "get", "marker_frequency") # Частота маркера
peak_freq = MOKO.Driver(SA, "get", "SCPI = CALC:MARK:X?")  # Прямая SCPI

peak_level = MOKO.Driver(SA, "get", "marker_level")    # Уровень маркера
peak_level = MOKO.Driver(SA, "get", "SCPI = CALC:MARK:Y?")  # Прямая SCPI

# --- Спектральная маска ------------------------------------------------------
MOKO.Driver(SA, "set", "limit_mask = ON")              # Включение проверки маски
MOKO.Driver(SA, "set", "SCPI = CALC:LIM:STAT ON")      # Прямая SCPI

mask_result = MOKO.Driver(SA, "get", "limit_fail")     # Результат (0=OK, 1=FAIL)
mask_result = MOKO.Driver(SA, "get", "SCPI = CALC:LIM:FAIL?")  # Прямая SCPI