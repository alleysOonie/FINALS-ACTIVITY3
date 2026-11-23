const pictureInput = document.getElementById("picture-input");
const fileName = document.getElementById("file-name");
const uploadForm = document.getElementById("upload-form");

pictureInput?.addEventListener("change", () => {
  const file = pictureInput.files[0];
  if (file) {
    fileName.textContent = file.name;
    const reader = new FileReader();
    reader.onload = (event) => {
      document.querySelectorAll(".avatar, .top-actions img, .composer-row img, .post-author img, .photo-grid img")
        .forEach((img) => img.src = event.target.result);
    };
    reader.readAsDataURL(file);
  }
});
uploadForm?.addEventListener("submit", (event) => {
  const file = pictureInput.files[0];
  if (!file) {
    event.preventDefault();
    alert("Please select a profile picture first.");
  } else if (!file.type.startsWith("image/")) {
    event.preventDefault();
    alert("Please select a valid image.");
  } else if (file.size > 5 * 1024 * 1024) {
    event.preventDefault();
    alert("The image must be 5 MB or smaller.");
  }
});
