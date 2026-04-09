import MOKO

# =============================================================================
# R&S ГЕНЕРАТОР СИГНАЛОВ
# =============================================================================

SG = "RS_SIGNAL_GENERATOR"

# =============================================================================
# ГРУППА 1: ИНИЦИАЛИЗАЦИЯ
# =============================================================================

idn = MOKO.Driver(SG, "init")                              # Идентификация
MOKO.Driver(SG, "set", "# *RST")                           # Сброс
MOKO.Driver(SG, "set", "# *CLS")                           # Очистка ошибок

# =============================================================================
# ГРУППА 2: ПЕРВИЧНАЯ НАСТРОЙКА СИГНАЛА
# =============================================================================

MOKO.Driver(SG, "set", "freqmode = CW")                    # Режим частоты CW | SWEEP | LIST
MOKO.Driver(SG, "set", "# SOUR:FREQ:MODE CW")              # SCPI (CW | SWEEP | LIST)

MOKO.Driver(SG, "set", "frequency = 2.8GHz")               # Частота 2.8GHz | 1.5GHz | 100MHz
MOKO.Driver(SG, "set", "# SOUR:FREQ 2.8GHz")               # SCPI (2.8GHz | 1.5GHz | 100MHz)

MOKO.Driver(SG, "set", "power = -50dBm")                   # Мощность -50dBm | -30dBm | 0dBm
MOKO.Driver(SG, "set", "# SOUR:POW -50dBm")                # SCPI (-50dBm | -30dBm | 0dBm)

MOKO.Driver(SG, "set", "arb_reset")                        # Сброс ARB
MOKO.Driver(SG, "set", "# SOUR:BB:ARB:PRESet")             # SCPI (без параметров)

MOKO.Driver(SG, "set", "waveform = WCDMAFast")             # Выбор волны WCDMAFast | LTE | 5G
MOKO.Driver(SG, "set", "# SOUR:BB:ARB:WAV:SEL 'WCDMAFast'") # SCPI ('WCDMAFast' | 'LTE' | '5G')

MOKO.Driver(SG, "set", "arb_state = ON")                   # ARB состояние ON | OFF
MOKO.Driver(SG, "set", "# SOUR:BB:ARB:STAT ON")            # SCPI (ON | OFF)

# =============================================================================
# ГРУППА 3: УПРАВЛЕНИЕ И ИЗМЕНЕНИЯ
# =============================================================================

MOKO.Driver(SG, "set", "output = ON")                      # Включение/выключение выхода ON | OFF
MOKO.Driver(SG, "set", "# OUTP ON")                        # SCPI (ON | OFF)

MOKO.Driver(SG, "set", "power = -30dBm")                   # Динамическое изменение мощности
MOKO.Driver(SG, "set", "# SOUR:POW -30dBm")                # SCPI (-30dBm | -25dBm | -20dBm)

MOKO.Driver(SG, "set", "frequency = 2.9GHz")               # Динамическое изменение частоты
MOKO.Driver(SG, "set", "# SOUR:FREQ 2.9GHz")               # SCPI (2.9GHz | 3.0GHz | 3.1GHz)

# =============================================================================
# ГРУППА 4: ЗАПРОСЫ (GET)
# =============================================================================

error = MOKO.Driver(SG, "get", "# SYST:ERR?")              # Запрос ошибки (возвращает "0,No error")

output_state = MOKO.Driver(SG, "get", "output")            # Запрос состояния выхода
output_state = MOKO.Driver(SG, "get", "# OUTP?")           # SCPI (возвращает 1 | 0)

power_now = MOKO.Driver(SG, "get", "power")                # Запрос текущей мощности
power_now = MOKO.Driver(SG, "get", "# SOUR:POW?")          # SCPI (возвращает -50.0)

freq_now = MOKO.Driver(SG, "get", "frequency")             # Запрос текущей частоты
freq_now = MOKO.Driver(SG, "get", "# SOUR:FREQ?")          # SCPI (возвращает 2800000000)