"""add_channel_id_column

Revision ID: e3625bacf6f9
Revises: 7c76d64526a7
Create Date: 2025-07-16 12:24:14.203777

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e3625bacf6f9"
down_revision = "7c76d64526a7"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("notification", schema=None) as batch_op:
        batch_op.add_column(sa.Column("channel_id", sa.Integer(), nullable=True))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("notification", schema=None) as batch_op:
        batch_op.drop_column("channel_id")
