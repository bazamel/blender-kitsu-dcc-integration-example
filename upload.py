import gazu

# Connect to your local Kitsu instance
gazu.set_host("http://localhost/api")

# Authenticate
user = gazu.log_in("admin@example.com", "mysecretpassword")

print("Logged in as:", user["first_name"])

tasks = gazu.task.all_tasks_for_asset(asset_dict)
task_status = gazu.task.get_task_status_by_short_name("wip")

(comment, preview_file) = gazu.task.publish_preview(
    task,
    wip,
    comment="Change status to work in progress",
    preview_file_path="./thumbnail.png"
)