"""create books table

Revision ID: b70998025735
Revises: 
Create Date: 2023-04-08 07:01:39.136192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b70998025735"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column(
            "id", sa.Integer(), autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("books")
