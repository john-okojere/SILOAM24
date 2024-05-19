// Get the video element
const videoElement = document.getElementById('bgVideo');

// Array of video sources
const videoSources = [
    'videos/1.mp4',
    'videos/3.mp4',
    'videos/2.mp4'
];

// Initialize index for tracking current video
let currentVideoIndex = 0;

// Function to change the video source
function changeVideo() {
    // Add fade-out class to initiate fade-out effect
    videoElement.classList.add('fade-out');

    setTimeout(() => {
        // Set the video source to the next video in the array
        videoElement.src = videoSources[currentVideoIndex];

        // Increment the index for the next iteration
        currentVideoIndex++;

        // Reset index to 0 if it exceeds the length of the array
        if (currentVideoIndex >= videoSources.length) {
            currentVideoIndex = 0;
        }

        // Remove fade-out class to initiate fade-in effect
        videoElement.classList.remove('fade-out');

        // Play the video
        videoElement.play();
    }, 1000); // Wait for the transition to complete (1 second)
}

// Listen for the 'timeupdate' event on the video element
videoElement.addEventListener('timeupdate', function() {
    // Check if the current time is close to the end of the video
    if (videoElement.currentTime >= videoElement.duration - 1) {
        // Call the function to change the video
        changeVideo();
    }
});

// Initial call to start playing the first video
changeVideo();
