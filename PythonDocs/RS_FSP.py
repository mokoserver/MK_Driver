import MOKO

# =============================================================================
# R&S АНАЛИЗАТОР СПЕКТРА (Rohde & Schwarz FSP30)
# =============================================================================

SA = "RS_FSP"

# =============================================================================
# ГРУППА 1: ИНИЦИАЛИЗАЦИЯ
# =============================================================================

idn = MOKO.Driver(SA, "init")                              # Идентификация
MOKO.Driver(SA, "set", "# *RST")                           # Сброс
MOKO.Driver(SA, "set", "# *CLS")                           # Очистка ошибок

# =============================================================================
# ГРУППА 2: ПЕРВИЧНАЯ НАСТРОЙКА (ЧАСТОТА/СПАН/УРОВЕНЬ)
# =============================================================================

MOKO.Driver(SA, "set", "center_freq = 2.8GHz")             # Центральная частота 2.8GHz | 1.5GHz | 100MHz
MOKO.Driver(SA, "set", "# FREQ:CENT 2.8GHz")               # SCPI (2.8GHz | 1.5GHz | 100MHz)

MOKO.Driver(SA, "set", "span = 35MHz")                     # Диапазон обзора 35MHz | 50MHz | 100MHz
MOKO.Driver(SA, "set", "# FREQ:SPAN 35MHz")                # SCPI (35MHz | 50MHz | 100MHz)

MOKO.Driver(SA, "set", "ref_level = 0dBm")                 # Опорный уровень 0dBm | -10dBm | -20dBm
MOKO.Driver(SA, "set", "# DISP:TRAC:Y:RLEV 0dBm")          # SCPI (0dBm | -10dBm | -20dBm)

# =============================================================================
# ГРУППА 3: НАСТРОЙКА ПОЛОС (RBW/VBW)
# =============================================================================

MOKO.Driver(SA, "set", "rbw_auto = OFF")                   # Автоматический RBW ON | OFF
MOKO.Driver(SA, "set", "# BAND:AUTO OFF")                  # SCPI (ON | OFF)

MOKO.Driver(SA, "set", "rbw = 5kHz")                       # Полоса разрешения RBW 5kHz | 10kHz | 100kHz
MOKO.Driver(SA, "set", "# BAND 5kHz")                      # SCPI (5kHz | 10kHz | 100kHz)

MOKO.Driver(SA, "set", "vbw_auto = OFF")                   # Автоматический VBW ON | OFF
MOKO.Driver(SA, "set", "# BAND:VID:AUTO OFF")              # SCPI (ON | OFF)

MOKO.Driver(SA, "set", "vbw = 50kHz")                      # Полоса видео VBW 50kHz | 100kHz | 500kHz
MOKO.Driver(SA, "set", "# BAND:VID 50kHz")                 # SCPI (50kHz | 100kHz | 500kHz)

# =============================================================================
# ГРУППА 4: НАСТРОЙКА ДЕТЕКТОРА
# =============================================================================

MOKO.Driver(SA, "set", "detector = RMS")                   # Тип детектора RMS | MAX | MIN | SAMPLE
MOKO.Driver(SA, "set", "# DET RMS")                        # SCPI (RMS | MAX | MIN | SAMPLE)

# =============================================================================
# ГРУППА 5: НАСТРОЙКА ИЗМЕРЕНИЯ МОЩНОСТИ КАНАЛА
# =============================================================================

MOKO.Driver(SA, "set", "channel_bw = 5MHz")                # Ширина канала 5MHz | 10MHz | 20MHz
MOKO.Driver(SA, "set", "# SENS:POW:ACH:BWID 5MHz")         # SCPI (5MHz | 10MHz | 20MHz)

MOKO.Driver(SA, "set", "ach_mode = ABS")                   # Режим ACH ABS | REL | ACP
MOKO.Driver(SA, "set", "# SENS:POW:ACH:MODE ABS")          # SCPI (ABS | REL | ACP)

MOKO.Driver(SA, "set", "measure_type = CPOW")              # Тип измерения CPOW | ACP | OBW
MOKO.Driver(SA, "set", "# CALC:MARK:FUNC:POW:SEL CPOW")    # SCPI (CPOW | ACP | OBW)

# =============================================================================
# ГРУППА 6: УПРАВЛЕНИЕ ИЗМЕРЕНИЯМИ
# =============================================================================

MOKO.Driver(SA, "set", "cont_sweep = OFF")                 # Непрерывная развертка ON | OFF
MOKO.Driver(SA, "set", "# INIT:CONT OFF")                  # SCPI (ON | OFF)

MOKO.Driver(SA, "set", "display_update = OFF")             # Обновление дисплея ON | OFF
MOKO.Driver(SA, "set", "# INIT:DISP OFF")                  # SCPI (ON | OFF)

MOKO.Driver(SA, "set", "init_sweep")                       # Запуск развертки (однократно)
MOKO.Driver(SA, "set", "# INIT")                           # SCPI (без параметров)

# =============================================================================
# ГРУППА 7: ЗАПРОСЫ (GET)
# =============================================================================

error = MOKO.Driver(SA, "get", "# SYST:ERR?")              # Запрос ошибки (возвращает "0,No error")

channel_power = MOKO.Driver(SA, "get", "channel_power")    # Запрос мощности канала
channel_power = MOKO.Driver(SA, "get", "# CALC:MARK:FUNC:POW:RES? CPOW") # SCPI (возвращает -25.5)