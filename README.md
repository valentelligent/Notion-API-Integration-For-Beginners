# Notion API Integration

This project demonstrates how to use the Notion API to create a parent page and a database within a Notion workspace. The integration is built using Python and the `notion-client` library.

## Prerequisites

- **Python Version**: 3.7 or higher
- **Notion Account**: Required to create and manage integrations
- **Notion Integration**: Must have the necessary permissions to create pages and databases

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/notion_api_integration.git
cd notion_api_integration
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Notion integration token:

```env
NOTION_TOKEN=your_integration_token
```

### 5. Run the Script

```bash
python src/main.py
```

## Code Explanation

### `src/main.py`

This script performs the following tasks:

- **Initialize Notion Client**: Connects to the Notion API using the provided integration token.

- **Create Parent Page**: Creates a new page in the specified workspace to serve as a parent for the database.

- **Create Database**: Creates a new database within the parent page with specified properties.

#### Key Functions

- `create_parent_page()`: Creates a parent page in the workspace using the provided page ID.

- `create_notes_database(parent_id)`: Creates a database within the parent page with properties like Name, Content, Tags, and Created.

## Notion API Details

- **API Version**: The integration uses the latest version of the Notion API as of November 2024.

- **Compatibility**: Ensure your integration has the necessary capabilities to create and manage pages and databases. Refer to the [Notion API Capabilities](https://developers.notion.com/reference/capabilities) for more information.

- **Parenting Rules**: Databases must be parented by pages when created via the API. Refer to the [Notion API Parent Object](https://developers.notion.com/reference/parent-object) for more details.

## Troubleshooting

- **Error: Could not find page with ID**: Ensure the page ID is correct and the page is shared with your integration.

- **Error: body failed validation**: Check the property schema and ensure it matches the expected format.

## References

- [Notion API Reference](https://developers.notion.com/reference/)
- [Notion API Parent Object](https://developers.notion.com/reference/parent-object)
- [Notion API Capabilities](https://developers.notion.com/reference/capabilities)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
