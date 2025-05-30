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
    y: int = None
    z: int = None


point1 = Point1D(x=10)
point2 = Point(x=10, y=25)
point3 = Point3D(x=10, y=25, z=11)


# Сериализация со значением по умолчанию
print(PointSchema.model_validate(point1).model_dump_json(indent=4))
print(PointSchema.model_validate(point2).model_dump_json(indent=4))
print(PointSchema.model_validate(point3).model_dump_json(indent=4))

