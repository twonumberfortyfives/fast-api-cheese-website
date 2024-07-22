from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd3d616d2a318'
down_revision: Union[str, None] = 'c08cdcb3cb81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Use batch mode for SQLite
    with op.batch_alter_table('cheese', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_cheese_title', ['title'])


def downgrade() -> None:
    # Use batch mode for SQLite
    with op.batch_alter_table('cheese', schema=None) as batch_op:
        batch_op.drop_constraint('uq_cheese_title', type_='unique')
