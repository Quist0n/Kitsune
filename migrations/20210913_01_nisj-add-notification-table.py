
"""
Add notification table with indexes
"""
from yoyo import step
__depends__ = {"20210814_01_xwCee_add_role_column_to_accounts_table"}

steps = [
    step(
    """
    CREATE TYPE notification_types as ENUM ('none', 'artist_updated', 'account_promotion', 'account_demotion', 'administrative');
    CREATE TABLE IF NOT EXISTS notification (
        id BIGSERIAL PRIMARY KEY,
        account_id INT NOT NULL,
        type notification_types NOT NULL DEFAULT 'none',
        categories text[] NOT NULL,
        extra_info jsonb,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES account(id)
    );

    CREATE INDEX IF NOT EXISTS notification_account_id_idx ON notification USING BTREE ("account_id");
    CREATE INDEX IF NOT EXISTS notification_created_at_idx ON notification USING BTREE ("created_at");
    CREATE INDEX IF NOT EXISTS notification_type_idx ON notification USING BTREE ("type");
    CREATE INDEX IF NOT EXISTS notification_categories_idx ON notification USING GIN ("categories");
    CREATE INDEX IF NOT EXISTS notification_extra_info_idx ON notification USING GIN ("extra_info");
    """,

    """
    DROP TYPE notification_types;
    DROP TABLE IF EXISTS notification;
    DROP INDEX IF EXISTS notification_account_id_idx;
    DROP INDEX IF EXISTS notification_created_at_idx;
    DROP INDEX IF EXISTS notification_type_idx;
    DROP INDEX IF EXISTS notification_categories_idx;
    DROP INDEX IF EXISTS notification_extra_info_idx;
    """
    )
    ]
