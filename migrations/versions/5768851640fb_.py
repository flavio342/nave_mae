"""empty message

Revision ID: 5768851640fb
Revises: 35db552856f9
Create Date: 2020-04-05 14:02:44.659647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5768851640fb'
down_revision = '35db552856f9'
branch_labels = None
depends_on = None


def upgrade():
    print("oi")


def downgrade():
    print("vlw")
