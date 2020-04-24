"""empty message

Revision ID: 7378aceabfb1
Revises: 53872c18a2de
Create Date: 2020-04-23 15:25:50.108504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7378aceabfb1'
down_revision = '53872c18a2de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todo', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todo', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###