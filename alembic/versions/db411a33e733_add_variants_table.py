"""add_variants_table

Revision ID: db411a33e733
Revises: 4b0fcd8d942a
Create Date: 2025-02-26 03:06:07.737107

"""
from typing import Sequence, Union
from sqlalchemy.dialects import postgresql
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db411a33e733'
down_revision: Union[str, None] = '4b0fcd8d942a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'variants',
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('field_id', postgresql.UUID(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['field_id'], ['field.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('variants')
    # ### end Alembic commands ###