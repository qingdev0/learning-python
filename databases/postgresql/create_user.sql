-- Function to create app schema and user with permissions if they don't exist
-- Returns 'created' if user was created, 'existed' if user already exists
DO $$
DECLARE
    user_exists BOOLEAN;
    schema_exists BOOLEAN;
    result_status TEXT;
BEGIN
    -- Check if user already exists
    SELECT EXISTS(SELECT 1 FROM pg_roles WHERE rolname = 'app_user') INTO user_exists;

    -- Check if schema already exists
    SELECT EXISTS(SELECT 1 FROM information_schema.schemata WHERE schema_name = 'app_schema') INTO schema_exists;

    -- Set initial result
    result_status := 'existed';

    -- Create schema if it doesn't exist
    IF NOT schema_exists THEN
        CREATE SCHEMA app_schema;
        RAISE NOTICE 'Schema app_schema created';
    ELSE
        RAISE NOTICE 'Schema app_schema already exists';
    END IF;

    -- Create user if it doesn't exist
    IF NOT user_exists THEN
        CREATE USER app_user WITH PASSWORD 'app_password';
        result_status := 'created';
        RAISE NOTICE 'User app_user created';
    ELSE
        RAISE NOTICE 'User app_user already exists';
    END IF;

    -- Grant privileges (will execute regardless if user exists or not)
    GRANT USAGE ON SCHEMA app_schema TO app_user;
    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA app_schema TO app_user;
    GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA app_schema TO app_user;

    -- Set default privileges for future tables
    ALTER DEFAULT PRIVILEGES IN SCHEMA app_schema
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;

    ALTER DEFAULT PRIVILEGES IN SCHEMA app_schema
    GRANT USAGE, SELECT ON SEQUENCES TO app_user;

    -- Return the result status to the caller
    RAISE NOTICE 'RESULT:%', result_status;
END $$;
