from pydantic import BaseModel, AnyHttpUrl, ConfigDict, AnyUrl

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'avatar': 'path/to/avatar.jpg',
    'email': '1@3.com',
    'phone': '1234567890',
    'address': '123 Main St, New York, NY 10001',
    'company': 'Example Corp',
    'job_title': 'Software Engineer',
    'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'website': 'https://example.com',
    'social_media': {
        'facebook': 'https://facebook.com/example',
        'twitter': 'https://twitter.com/example',
        'linkedin': 'https://linkedin.com/in/example',
    },
    'interests': ['coding', 'music', 'sports'],
    'skills': ['Python', 'Django', 'JavaScript'],
    'education': [
        {
            'degree': 'Bachelor of Science in Computer Science',
            'institution': 'University of Example',
            'year': 2015,
        },
        {
            'degree': 'Master of Science in Software Engineering',
            'institution': 'Example University',
            'year': 2017,
        },
    ],
}
class UserSocialMedia(BaseModel):
    facebook: AnyUrl
    twitter: AnyUrl
    linkedin: AnyUrl

class User(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str
    age: int
    city: str
    avatar: str
    email: str
    phone: str
    address: str
    company: str
    job_title: str
    bio: str
    website: str
    social_media: UserSocialMedia
    interests: list[str]
    skills: list[str]
    education: list[dict[str, str | int]]

    def __str__(self):
        return f"User(name={self.name}, age={self.age}, city={self.city}, email={self.email})"



user = User.model_validate(data)
print(user)

class Task:
    __slots__ = ('title', 'description', 'status', 'id')
    def __init__(self, title: str, description: str, status: str, id: int):
        self.title = title
        self.description = description
        self.status = status
        self.id = id