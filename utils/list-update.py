from sqlalchemy import create_engine, Column, Integer, String, Boolean, exists
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from time import time
from requests import head

AD_LISTS_FILE = "/etc/pihole/adlists.list"


engine = create_engine(
    "sqlite:////etc/pihole/gravity.db",
    echo=False,
    future=True,
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Adlist_repo(Base):
    __tablename__ = "adlist"

    id = Column(Integer, primary_key=True)
    address = Column(String(100))
    enabled = Column(Boolean)
    date_added = Column(Integer)
    comment = String(100)


def url_exists(url):
    response = head(url.strip())
    if response.status_code < 400:
        return True
    else:
        return False


def url_in_db(session, Adlist_repo, url):
    return session.query(exists().where(Adlist_repo.address == url.strip())).scalar()


def add_to_db(session, Adlist_repo, url):
    adlist = Adlist_repo(
        address=url.strip(),
        enabled=True,
        date_added=int(time()),
    )
    session.add(adlist)
    session.commit()


def main():
    with open(AD_LISTS_FILE) as ad_lists_file:
        for ad_list in ad_lists_file.readlines():
            if url_exists(ad_list) and not url_in_db(session, Adlist_repo, ad_list):
                print(f"Adding URL to DB: {ad_list}")
                add_to_db(session, Adlist_repo, ad_list)
            elif not url_exists(ad_list):
                print(f"URL doesn't exist: {ad_list}")
            elif url_in_db(session, Adlist_repo, ad_list):
                print(f"URL already in the database: {ad_list}")


if __name__ == "__main__":
    main()
