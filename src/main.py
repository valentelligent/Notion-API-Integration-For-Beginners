import os
from dotenv import load_dotenv
from notion_client import Client

# Load environment variables
load_dotenv()

# Initialize the Notion client
notion = Client(auth=os.getenv("NOTION_TOKEN"))

def create_parent_page():
    """Create a parent page in the workspace"""
    try:
        print("\nCreating parent page...")
        page = notion.pages.create(
            parent={
                "type": "page_id",
                "page_id": "13c12ce344d980fb8984d34682b49b5d"  # Corrected page ID
            },
            properties={
                "title": {
                    "title": [
                        {
                            "text": {
                                "content": "Notes Workspace"
                            }
                        }
                    ]
                }
            }
        )
        print("✅ Successfully created parent page")
        print(f"Page ID: {page['id']}")
        return page["id"]
    except Exception as e:
        print(f"❌ Error creating parent page: {str(e)}")
        return None

def create_notes_database(parent_id):
    """Create a new database in the parent page"""
    try:
        print("\nCreating database...")
        new_database = notion.databases.create(
            parent={
                "type": "page_id",
                "page_id": parent_id
            },
            title=[
                {
                    "type": "text",
                    "text": {
                        "content": "Notes Database"
                    }
                }
            ],
            properties={
                "Name": {
                    "title": {}
                },
                "Content": {
                    "rich_text": {}
                },
                "Tags": {
                    "multi_select": {
                        "options": [
                            {"name": "test", "color": "blue"},
                            {"name": "api", "color": "green"}
                        ]
                    }
                },
                "Created": {
                    "created_time": {}
                }
            }
        )
        print("✅ Successfully created database")
        print(f"Database ID: {new_database['id']}")
        return new_database["id"]
    except Exception as e:
        print(f"❌ Error creating database: {str(e)}")
        return None

if __name__ == "__main__":
    print("Setting up Notion workspace...")
    parent_id = create_parent_page()
    if parent_id:
        database_id = create_notes_database(parent_id)
        if database_id:
            print("\nSetup complete!")
