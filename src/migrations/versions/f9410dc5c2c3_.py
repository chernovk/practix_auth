"""empty message

Revision ID: f9410dc5c2c3
Revises: c40287b2eb7a
Create Date: 2021-11-09 11:24:49.606099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9410dc5c2c3'
down_revision = 'c40287b2eb7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'history', ['id'])
    op.drop_constraint('history_user_id_fkey', 'history', type_='foreignkey')
    op.create_foreign_key(None, 'history', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_unique_constraint(None, 'user', ['id'])
    op.drop_constraint('user_role_id_fkey', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_foreign_key('user_role_id_fkey', 'user', 'role', ['role_id'], ['id'])
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'history', type_='foreignkey')
    op.create_foreign_key('history_user_id_fkey', 'history', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'history', type_='unique')
    # ### end Alembic commands ###
