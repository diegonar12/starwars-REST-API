"""empty message

Revision ID: 0e1be0234ae5
Revises: a3ccbfd1e2c7
Create Date: 2025-02-01 03:52:22.329626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e1be0234ae5'
down_revision = 'a3ccbfd1e2c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_added', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('favorite_type', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('note', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('height', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('mass', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('hair_color', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('birth_year', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('homeworld', sa.String(length=120), nullable=True))

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('climate', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('population', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('terrain', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('orbital_period', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('rotation_period', sa.String(length=120), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('first_name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')
        batch_op.drop_column('username')

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_column('rotation_period')
        batch_op.drop_column('orbital_period')
        batch_op.drop_column('terrain')
        batch_op.drop_column('population')
        batch_op.drop_column('climate')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_column('homeworld')
        batch_op.drop_column('birth_year')
        batch_op.drop_column('hair_color')
        batch_op.drop_column('mass')
        batch_op.drop_column('height')
        batch_op.drop_column('gender')

    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.drop_column('is_active')
        batch_op.drop_column('note')
        batch_op.drop_column('favorite_type')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('date_added')

    # ### end Alembic commands ###
