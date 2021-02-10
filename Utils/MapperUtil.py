
def mapper_util(giver: object, recipient: object) -> object:
    if hasattr(giver, "__table__"):
        for c in giver.__table__.columns:
            if getattr(giver, c.name) is not None :
                setattr(recipient, c.name, getattr(giver, c.name, None))
        return recipient
    else:
        return None


if __name__ == "__main__":
    from FirstService.First import First
    from Entity import Entity
    recipient = First(id=3, guid=4, version=3)
    giver = First(id=3, guid=5)
    recipient = mapper_util(giver, recipient)
    print(recipient.__table__.columns)
    print(recipient.guid)
    print(recipient.version)

    much = First(id=3, guid=4, version=3, address="abc")
    less = Entity(id=3, guid=5)
    recipient = mapper_util(less, much)
    print(type(recipient))

