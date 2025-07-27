
# LibraryProject
This is a Django project for managing a library system.
# Permission & Group Setup - LibraryProject

## Custom Permissions (defined in models.py):
- can_view: View book list/details
- can_create: Add new books
- can_edit: Update existing books
- can_delete: Remove books

## Groups and Permissions:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Setup Notes:
- Permissions are enforced in views using @permission_required
- Groups can be managed via the Django admin panel
- Users should be assigned to appropriate groups based on their role
