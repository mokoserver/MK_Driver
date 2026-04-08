import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# =============================================================================
# RS_SMVB100A — Векторный генератор сигналов (Rohde & Schwarz)
# Аналог для RFTEX_RTVG20
# IP: 169.254.1.122
# =============================================================================

# Присвоение имени драйвера
VSG = "RS_SMVB100A"

# --- Инициализация и сброс ---------------------------------------------------
MOKO.Driver(VSG, "set", "*RST")                          # Сброс в заводские настройки
MOKO.Driver(VSG, "set", "*CLS")                          # Очистка очереди ошибок
idn = MOKO.Driver(VSG, "get", "*IDN?")                   # Идентификация прибора

# --- Несущая частота и мощность ----------------------------------------------
MOKO.Driver(VSG, "set", "frequency = 2400000000")        # Несущая частота 2.4 ГГц
MOKO.Driver(VSG, "set", "SCPI = FREQ 2400000000")        # Прямая SCPI (R&S синтаксис)

MOKO.Driver(VSG, "set", "power = -10")                   # Мощность -10 дБм
MOKO.Driver(VSG, "set", "SCPI = POW -10")                # Прямая SCPI (R&S синтаксис)

MOKO.Driver(VSG, "set", "output = ON")                   # Включение ВЧ-выхода
MOKO.Driver(VSG, "set", "output = OFF")                  # Выключение ВЧ-выхода
MOKO.Driver(VSG, "set", "SCPI = OUTP ON")                # Прямая SCPI (R&S синтаксис)

# --- Импульсный режим --------------------------------------------------------
MOKO.Driver(VSG, "set", "pulse_mode = ON")               # Включение импульсного режима
MOKO.Driver(VSG, "set", "SCPI = PULM:STAT ON")           # Прямая SCPI

MOKO.Driver(VSG, "set", "pulse_width = 0.0001")          # Длительность импульса 100 мкс
MOKO.Driver(VSG, "set", "SCPI = PULM:WIDT 100US")        # Прямая SCPI

MOKO.Driver(VSG, "set", "pulse_period = 0.001")          # Период импульса 1 мс
MOKO.Driver(VSG, "set", "SCPI = PULM:PER 1MS")           # Прямая SCPI

# --- Цифровая модуляция ------------------------------------------------------
MOKO.Driver(VSG, "set", "modulation_type = QPSK")        # Тип модуляции QPSK
MOKO.Driver(VSG, "set", "SCPI = SOUR:BB:DM:TYPE QPSK")   # Прямая SCPI (R&S синтаксис)

MOKO.Driver(VSG, "set", "symbol_rate = 400000000")       # Символьная скорость 400 Мсимв/с
MOKO.Driver(VSG, "set", "SCPI = SOUR:BB:DM:SRAT 400E6")  # Прямая SCPI (R&S синтаксис)

MOKO.Driver(VSG, "set", "filter_type = RRC")             # Формирующий фильтр RRC
MOKO.Driver(VSG, "set", "SCPI = SOUR:BB:DM:FILT:TYPE RRC")  # Прямая SCPI (R&S синтаксис)

MOKO.Driver(VSG, "set", "filter_alpha = 0.35")           # Коэффициент сглаживания
MOKO.Driver(VSG, "set", "SCPI = SOUR:BB:DM:FILT:RRC:ALPH 0.35")  # Прямая SCPI

# --- Генератор шума (AWGN) ---------------------------------------------------
MOKO.Driver(VSG, "set", "noise_mode = ON")               # Включение AWGN
MOKO.Driver(VSG, "set", "SCPI = SOUR:BB:NOIS:STAT ON")   # Прямая SCPI (R&S синтаксис)

MOKO.Driver(VSG, "set", "c_n_ratio = 30")                # Отношение C/N = 30 дБ
MOKO.Driver(VSG, "set", "SCPI = SOUR:BB:NOIS:CN 30")     # Прямая SCPI (R&S синтаксис)

# --- Ожидание готовности -----------------------------------------------------
MOKO.Driver(VSG, "set", "*OPC?")                         # Ожидание завершения операций