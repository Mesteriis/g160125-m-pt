from pydantic import BaseModel, ConfigDict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Point1D:
    def __init__(self, x):
        self.x = x


class PointSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    x: int
    y: int


# TODO-1: поменяйте значение координат: int -> float
# TODO-2: поменяйте значение координат: int -> str
point = Point(x=10, y=25)
# TODO-3: создайте экземпляр класса Point3D, попробуйте его сериализовать через PointSchema
# TODO-4: создайте экземпляр класса Point1D, попробуйте его сериализовать через PointSchema
schema = PointSchema.model_validate(point)
point_json = schema.model_dump_json(indent=4)

print(point_json)


# TODO-3: создаём экземпляр класса Point3D и сериализуем
# point3d = Point3D(x=1, y=2, z=3)
# try:
#     schema_3d = PointSchema.model_validate(point3d)
#     point3d_json = schema_3d.model_dump_json(indent=4)
#     print("Point3D:\n", point3d_json)
# except Exception as e:
#     print("Validation error for Point3D:", e)


# TODO-4: создаём экземпляр класса Point1D и сериализуем
# point1d = Point1D(x=100)
# try:
#     schema_1d = PointSchema.model_validate(point1d)
#     point1d_json = schema_1d.model_dump_json(indent=4)
#     print("Point1D:\n", point1d_json)
# except Exception as e:
#     print("Validation error for Point1D:", e)
