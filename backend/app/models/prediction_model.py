from sqlalchemy import Column, String, Float, Integer, DateTime
from datetime import datetime, timezone
from backend.app.database import Base


class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key = True,index= True)
    emotion = Column(String, nullable=True)
    confidence = Column(Float, nullable=True)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
