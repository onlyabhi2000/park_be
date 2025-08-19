
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from configuration.db import get_db, Base
from dependencies.role_deps import owner_required
from models.owner import Owner
from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/abhishek/parking_lot_app/.env")

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_owner_required():
    db = TestingSessionLocal()
    try:
        # Create a dummy owner for testing purposes
        owner = db.query(Owner).filter(Owner.email == "testowner@example.com").first()
        if not owner:
            owner = Owner(
                name="Test Owner",
                email="testowner@example.com",
                password="password"
            )
            db.add(owner)
            db.commit()
            db.refresh(owner)
        return owner
    finally:
        db.close()


@pytest.fixture(scope="function")
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[owner_required] = override_owner_required
    with TestClient(app) as c:
        yield c

