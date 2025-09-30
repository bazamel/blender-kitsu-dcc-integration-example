import gazu

gazu.set_host("http://localhost/api")

user = gazu.log_in("admin@example.com", "mysecretpassword")

print("Logged in as:", user['user']['full_name'])

projects = gazu.project.all_projects()

assets = gazu.asset.all_assets_for_project(projects[0])

tasks = gazu.task.all_tasks_for_asset(assets[0])
task_status = gazu.task.get_task_status_by_short_name("todo")

(comment, preview_file) = gazu.task.publish_preview(
    tasks[0],
    task_status,
    comment="upload preview",
    preview_file_path="./thumbnail.png"
)