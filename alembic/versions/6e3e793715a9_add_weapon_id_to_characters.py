"""add_weapon_id_to_characters

Revision ID: 6e3e793715a9
Revises: 9e5ec58be09f
Create Date: 2025-02-27 10:00:44.570828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e3e793715a9'
down_revision: Union[str, None] = '9e5ec58be09f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('weapon_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'characters', type_='foreignkey')
    op.create_foreign_key(None, 'characters', 'weapons', ['weapon_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'characters', type_='foreignkey')
    op.create_foreign_key(None, 'characters', 'users', ['name'], ['username'])
    op.drop_column('characters', 'weapon_id')
    # ### end Alembic commands ###
