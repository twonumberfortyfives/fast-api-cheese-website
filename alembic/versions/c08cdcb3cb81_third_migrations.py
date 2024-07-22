"""third migrations

Revision ID: c08cdcb3cb81
Revises: d8f1ff1ae726
Create Date: 2024-07-22 20:18:35.896474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c08cdcb3cb81'
down_revision: Union[str, None] = 'd8f1ff1ae726'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
