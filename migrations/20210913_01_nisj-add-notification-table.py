
"""
Add notification table with indexes
"""
from yoyo import step
__depends__ = {"20210905_01_rjak-add_index_to_accounts_table"}

steps = [
    step(
    """
    CREATE TABLE IF NOT EXISTS notification (
        id BIGSERIAL PRIMARY KEY,
        account_id INT NOT NULL,
        type SMALLINT NOT NULL,
        extra_info jsonb,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES account(id)
    );

    CREATE INDEX IF NOT EXISTS notification_account_id_idx ON notification USING BTREE ("account_id");
    CREATE INDEX IF NOT EXISTS notification_created_at_idx ON notification USING BTREE ("created_at");
    CREATE INDEX IF NOT EXISTS notification_type_idx ON notification USING BTREE ("type");
    """,

    """
    DROP TABLE IF EXISTS notification;
    """
    )
    ]
