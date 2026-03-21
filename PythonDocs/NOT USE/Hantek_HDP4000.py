import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# =============================================================================
# Hantek_HDP4000 — Программируемый источник питания (Hantek)
# =============================================================================

# Присвоение имени драйвера
PSU = "Hantek_HDP4000"

# --- Инициализация и сброс ---------------------------------------------------
MOKO.Driver(PSU, "set", "*RST")                     # Сброс
MOKO.Driver(PSU, "set", "*CLS")                     # Очистка ошибок
idn = MOKO.Driver(PSU, "get", "*IDN?")              # Идентификация

# --- Установка параметров ----------------------------------------------------
MOKO.Driver(PSU, "set", "voltage = 12.0")           # Напряжение 12.0 В
MOKO.Driver(PSU, "set", "SCPI = VOLT 12.0")         # Прямая SCPI

MOKO.Driver(PSU, "set", "current_limit = 1.5")      # Ограничение тока 1.5 А
MOKO.Driver(PSU, "set", "SCPI = CURR 1.5")          # Прямая SCPI

# --- Защиты ------------------------------------------------------------------
MOKO.Driver(PSU, "set", "ocp = ON")                 # Защита по току (OCP)
MOKO.Driver(PSU, "set", "SCPI = PROT:OCP ON")       # Прямая SCPI

MOKO.Driver(PSU, "set", "ovp = ON")                 # Защита по напряжению (OVP)
MOKO.Driver(PSU, "set", "SCPI = PROT:OVP ON")       # Прямая SCPI

# --- Управление выходом ------------------------------------------------------
MOKO.Driver(PSU, "set", "output = ON")              # Включение выхода
MOKO.Driver(PSU, "set", "SCPI = OUTP ON")           # Прямая SCPI

MOKO.Driver(PSU, "set", "output = OFF")             # Выключение выхода
MOKO.Driver(PSU, "set", "SCPI = OUTP OFF")          # Прямая SCPI

# --- Измерения ---------------------------------------------------------------
voltage_actual = MOKO.Driver(PSU, "get", "voltage_measure")  # Фактическое напряжение
voltage_actual = MOKO.Driver(PSU, "get", "SCPI = MEAS:VOLT?")  # Прямая SCPI

current_actual = MOKO.Driver(PSU, "get", "current_measure")   # Фактический ток
current_actual = MOKO.Driver(PSU, "get", "SCPI = MEAS:CURR?")  # Прямая SCPI