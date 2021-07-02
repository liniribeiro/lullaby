from alembic import command

from lullaby.database.migrations.config import alembic_cfg


def revision():
    message = input("Nome da revisão:")
    command.revision(alembic_cfg, autogenerate=True, message=message)


def upgrade():
    print("Start Migration")
    command.upgrade(alembic_cfg, "head")
    print("End Migration")
