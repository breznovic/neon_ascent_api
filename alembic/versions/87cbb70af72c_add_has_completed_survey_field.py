"""add has_completed_survey field

Revision ID: 87cbb70af72c
Revises: 8c660547af86
Create Date: 2025-02-26 11:14:57.701848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87cbb70af72c'
down_revision: Union[str, None] = '8c660547af86'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table('characters') as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(), nullable=True))

def downgrade():
    with op.batch_alter_table('characters') as batch_op:
        batch_op.drop_column('status')
