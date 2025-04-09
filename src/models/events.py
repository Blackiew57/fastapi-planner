from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tag: list[str]
    location: str
    created_at: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "아.. 집에 가고싶다",
                "image": "path/to",
                "description": "아 진짜 하기 싫다",  # 여기 쉼표 추가
                "tags": ["#Homesick", "#IwannagoHone"],
                "location": "제1실습관 ",
            }
        }
    )

    