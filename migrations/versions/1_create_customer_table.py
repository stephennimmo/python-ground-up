"""create customer table

Revision ID: 1
Revises: 
Create Date: 2023-09-04 09:06:29.526916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision: str = '1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'customer',
        sa.Column('customer_id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.Text, nullable=False),
        sa.Column('middle_name', sa.Text),
        sa.Column('last_name', sa.Text, nullable=False),
        sa.Column('suffix', sa.Text),
        sa.Column('email', sau.EmailType, nullable=False, unique=True),
        sa.Column('phone', sa.Text)
    )


def downgrade() -> None:
    op.drop_table('customer')
