"""create menu table

Revision ID: 5152accf8e88
Revises: 
Create Date: 2025-01-19 15:08:17.529887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision: str = '5152accf8e88'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'menu',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=True),
        sa.Column('admin', sa.String(length=1), nullable=True),
        sa.Column('url', sa.String(length=15), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_menu_id'), 'menu', ['id'], unique=False)
    op.create_index(op.f('ix_menu_name'), 'menu', ['name'], unique=False)
    op.create_index(op.f('ix_menu_admin'), 'menu', ['admin'], unique=False)
    op.create_index(op.f('ix_menu_url'), 'menu', ['url'], unique=False)
    # ### end Alembic commands ###

    menu_table = table(
        'menu',
        column('id', sa.Integer),
        column('name', sa.String),
        column('admin', sa.String),
        column('url', sa.String),
        column('created_at', sa.DateTime),
        column('updated_at', sa.DateTime)
    )

    op.bulk_insert(
        menu_table,
        [
            {
                'name': 'アカウントマスター',
                'admin': '',
                'url': '/account',
                'created_at': '2025-01-19 15:08:17.529887',
                'updated_at': '2025-01-19 15:08:17.529887'
            },
            {
                'name': 'パスワード検索',
                'admin': '',
                'url': '/password',
                'created_at': '2025-01-19 15:08:17.529887',
                'updated_at': '2025-01-19 15:08:17.529887'
            },
            {
                'name': '仮登録済リスト',
                'admin': '',
                'url': '/autoregist',
                'created_at': '2025-01-19 15:08:17.529887',
                'updated_at': '2025-01-19 15:08:17.529887'
            },
            {
                'name': '各種設定',
                'admin': '1',
                'url': '/admin/setting',
                'created_at': '2025-01-19 15:08:17.529887',
                'updated_at': '2025-01-19 15:08:17.529887'
            },
        ]
    )

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_menu_url'), table_name='menu')
    op.drop_index(op.f('ix_menu_admin'), table_name='menu')
    op.drop_index(op.f('ix_menu_name'), table_name='menu')
    op.drop_index(op.f('ix_menu_id'), table_name='menu')
    op.drop_table('menu')
    # ### end Alembic commands ###
