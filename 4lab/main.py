from abc import ABC, abstractmethod
from datetime import datetime
import json


# ===== Базовый класс (интерфейс) =====
class LogRecord(ABC):
    def init(self, level, time, message):
        self.level = level
        self.time = time
        self.message = message

    @abstractmethod
    def parse(self):
        pass

    def str(self):
        return f"[{self.time.strftime('%Y-%m-%d %H:%M:%S')}] {self.level} {self.message}"


# ===== Формат 1 =====
class Format1Log(LogRecord):
    def init(self, raw):
        self.raw = raw
        self.parse()

    def parse(self):
        # fmt1 [2025-10-01 12:34:56] INFO: System started
        try:
            parts = self.raw.split(" ")
            time_str = parts[1][1:] + " " + parts[2][:-1]
            level = parts[3][:-1]
            message = " ".join(parts[4:])
            time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            super().init(level, time, message)
        except:
            raise ValueError("Неверный формат fmt1")


# ===== Формат 2 =====
class Format2Log(LogRecord):
    def init(self, raw):
        self.raw = raw
        self.parse()

    def parse(self):
        # fmt2 ERROR;2025/10/01-12:35;Disk full
        try:
            _, rest = self.raw.split(" ", 1)
            level, time_str, message = rest.split(";")
            time = datetime.strptime(time_str, "%Y/%m/%d-%H:%M")
            super().init(level, time, message)
        except:
            raise ValueError("Неверный формат fmt2")


# ===== JSON формат =====
class JsonLog(LogRecord):
    def init(self, raw):
        self.raw = raw
        self.parse()

    def parse(self):
        # json {"level": "...", "time": "...", "msg": "..."}
        try:
            data = json.loads(self.raw[5:])
            level = data["level"]
            time = datetime.fromisoformat(data["time"])
            message = data["msg"]
            super().init(level, time, message)
        except:
            raise ValueError("Неверный JSON лог")


# ===== Менеджер логов =====
class LogManager:
    def init(self):
        self.logs = []

    def add_log(self, raw):
        try:
            if raw.startswith("fmt1"):
                self.logs.append(Format1Log(raw))
            elif raw.startswith("fmt2"):
                self.logs.append(Format2Log(raw))
            elif raw.startswith("json"):
                self.logs.append(JsonLog(raw))
            else:
                print("Неизвестный формат:", raw)
        except ValueError as e:
            print("Ошибка:", e)

    def count_by_level(self, level):
        return sum(1 for log in self.logs if log.level == level)

    def list_by_level(self, level):
        return [log for log in self.logs if log.level == level]

    def range_by_time(self, start, end):
        return [log for log in self.logs if start <= log.time <= end]


# ===== Пример работы =====
manager = LogManager()

inputs = [
    "fmt1 [2025-10-01 12:34:56] INFO: System started",
    "fmt2 ERROR;2025/10/01-12:35;Disk full",
    "json {\"level\": \"WARNING\", \"time\": \"2025-10-01T12:36:00\", \"msg\": \"High load\"}"
]

for line in inputs:
    manager.add_log(line)

print("Количество ERROR:", manager.count_by_level("ERROR"))
print("\nWARNING логи:")
for log in manager.list_by_level("WARNING"):
    print(log)

print("\nЛоги в диапазоне:")
start = datetime.strptime("2025-10-01 12:30", "%Y-%m-%d %H:%M")
end = datetime.strptime("2025-10-01 13:00", "%Y-%m-%d %H:%M")
for log in manager.range_by_time(start, end):
    print(log)
