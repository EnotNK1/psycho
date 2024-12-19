"""add link in Test

Revision ID: dafba4de0693
Revises: 775238b67346
Create Date: 2024-12-17 14:18:49.864819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dafba4de0693'
down_revision: Union[str, None] = '775238b67346'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'link')
    # ### end Alembic commands ###