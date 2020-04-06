"""empty message

Revision ID: efe9cf8277cb
Revises: 759effbf4ce1
Create Date: 2020-04-04 08:36:40.730944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efe9cf8277cb'
down_revision = '759effbf4ce1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('class', sa.Column('photo', sa.String(length=250), nullable=True))
    op.drop_constraint(None, 'class', type_='foreignkey')
    op.drop_column('class', 'institution_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('class', sa.Column('institution_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'class', 'institution', ['institution_id'], ['id'])
    op.drop_column('class', 'photo')
    # ### end Alembic commands ###