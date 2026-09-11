"use strict";

/* =========================================================
   ELEMENTS
========================================================= */

const setupModal = document.getElementById("setupModal");

const enableMediaBtn =
    document.getElementById("enableMediaBtn");

const startInterviewBtn =
    document.getElementById("startInterviewBtn");

const roleSelect =
    document.getElementById("roleSelect");

const levelSelect =
    document.getElementById("levelSelect");

const cameraVideo =
    document.getElementById("cameraVideo");

const questionText =
    document.getElementById("questionText");

const questionCounter =
    document.getElementById("questionCounter");

const questionProgress =
    document.getElementById("questionProgress");

const answerInput =
    document.getElementById("answerInput");

const speakQuestionBtn =
    document.getElementById("speakQuestionBtn");

const voiceAnswerBtn =
    document.getElementById("voiceAnswerBtn");

const nextQuestionBtn =
    document.getElementById("nextQuestionBtn");

const endInterviewBtn =
    document.getElementById("endInterviewBtn");

const evaluationMessage =
    document.getElementById("evaluationMessage");

const warningCountElement =
    document.getElementById("warningCount");

const redAlert =
    document.getElementById("redAlert");

const alertTitle =
    document.getElementById("alertTitle");

const alertMessage =
    document.getElementById("alertMessage");

const gazeStatusIcon =
    document.getElementById("gazeStatusIcon");

const gazeStatusText =
    document.getElementById("gazeStatusText");

const tabStatusIcon =
    document.getElementById("tabStatusIcon");

const tabStatusText =
    document.getElementById("tabStatusText");

const resultScreen =
    document.getElementById("resultScreen");

const finalWarningCount =
    document.getElementById("finalWarningCount");

const resultSummary =
    document.getElementById("resultSummary");

const feedbackContainer =
    document.getElementById("feedbackContainer");

const restartInterviewBtn =
    document.getElementById("restartInterviewBtn");


/* =========================================================
   STATE
========================================================= */

let cameraStream = null;
let screenStream = null;

let recognition = null;

let interviewStarted = false;

let role = "Software Engineer";
let level = "Beginner";

let currentQuestion = "";

let questionNumber = 0;

const totalQuestions = 8;

let history = [];

let warningCount = 0;

let warningEvents = [];

let voiceListening = false;

let alertTimeout = null;

let fullscreenRequested = false;

let tabWarningActive = false;

let windowWarningActive = false;


/* =========================================================
   MEDIA STATE
========================================================= */

const mediaReady = {
    camera: false,
    microphone: false,
    screen: false
};


/* =========================================================
   SETUP
========================================================= */

async function enableMedia() {

    try {

        const stream =
            await navigator.mediaDevices.getUserMedia({
                video: true,
                audio: true
            });

        cameraStream = stream;

        cameraVideo.srcObject =
            cameraStream;

        mediaReady.camera = true;
        mediaReady.microphone = true;


        /* -----------------------------------------
           SCREEN SHARE
        ----------------------------------------- */

        try {

            screenStream =
                await navigator.mediaDevices.getDisplayMedia({
                    video: true,
                    audio: false
                });

            mediaReady.screen = true;

            const screenTrack =
                screenStream.getVideoTracks()[0];

            if (screenTrack) {

                screenTrack.addEventListener(
                    "ended",
                    handleScreenShareStopped
                );

            }

        } catch (error) {

            console.warn(
                "Screen sharing cancelled:",
                error
            );

            mediaReady.screen = false;

        }


        updateStartButton();

    } catch (error) {

        console.error(
            "Camera/microphone error:",
            error
        );

        showRedAlert(
            "Permission Required",
            "Please allow camera and microphone access.",
            false
        );

    }

}


/* =========================================================
   SCREEN SHARE STOPPED
========================================================= */

function handleScreenShareStopped() {

    mediaReady.screen = false;

    updateStartButton();

    if (interviewStarted) {

        registerWarning(
            "Screen Sharing Stopped",
            "Please keep screen sharing enabled during the interview."
        );

    }

}


/* =========================================================
   START BUTTON STATE
========================================================= */

function updateStartButton() {

    const ready =
        mediaReady.camera &&
        mediaReady.microphone &&
        mediaReady.screen;


    startInterviewBtn.disabled =
        !ready;


    if (ready) {

        startInterviewBtn.textContent =
            "Start AI Interview →";

        enableMediaBtn.textContent =
            "✓ Camera, Microphone & Screen Ready";

    } else {

        startInterviewBtn.textContent =
            "Enable Camera, Microphone & Screen";

    }

}


/* =========================================================
   FULLSCREEN
========================================================= */

async function enterInterviewFullscreen() {

    if (document.fullscreenElement) {

        fullscreenRequested = true;

        return true;
    }


    if (
        !document.documentElement.requestFullscreen
    ) {

        console.warn(
            "Fullscreen API is not supported."
        );

        return false;
    }


    try {

        /*
         * This function is called directly from the
         * Start Interview button click.
         *
         * That is important because browsers allow
         * fullscreen only from a user interaction.
         */

        await document.documentElement.requestFullscreen();

        fullscreenRequested = true;

        return true;

    } catch (error) {

        console.warn(
            "Fullscreen request failed:",
            error
        );

        fullscreenRequested = false;

        return false;
    }

}


/* =========================================================
   EXIT FULLSCREEN
========================================================= */

async function exitInterviewFullscreen() {

    if (!document.fullscreenElement) {
        return;
    }

    try {

        await document.exitFullscreen();

    } catch (error) {

        console.warn(
            "Could not exit fullscreen:",
            error
        );

    }

    fullscreenRequested = false;

}


/* =========================================================
   START INTERVIEW
========================================================= */

async function startInterview() {

    /*
     * IMPORTANT:
     * Request fullscreen immediately, before await fetch().
     */

    await enterInterviewFullscreen();


    role =
        (roleSelect.value || "Software Engineer")
            .trim();

    level =
        (levelSelect.value || "Beginner")
            .trim();


    try {

        const response =
            await fetch(
                "/api/interview/start",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        role: role,
                        level: level
                    })
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.error ||
                "Could not start interview."
            );

        }


        interviewStarted = true;

        history = [];

        warningCount = 0;

        warningEvents = [];

        questionNumber = 1;


        warningCountElement.textContent =
            "0";


        finalWarningCount.textContent =
            "0";


        currentQuestion =
            data.message ||
            "Please introduce yourself.";


        history.push({

            role: "assistant",

            content:
                currentQuestion

        });


        setupModal.classList.add(
            "hidden"
        );


        resultScreen.classList.add(
            "hidden"
        );


        displayQuestion(
            currentQuestion
        );


        startTabMonitoring();


    } catch (error) {

        console.error(
            "Interview start error:",
            error
        );


        await exitInterviewFullscreen();


        showRedAlert(
            "Interview Error",
            "Could not start the interview. Please try again.",
            false
        );

    }

}


/* =========================================================
   DISPLAY QUESTION
========================================================= */

function displayQuestion(question) {

    currentQuestion =
        question || "Please introduce yourself.";


    questionText.textContent =
        cleanQuestion(
            currentQuestion
        );


    questionCounter.textContent =
        `QUESTION ${questionNumber} / ${totalQuestions}`;


    updateQuestionProgress();


    answerInput.value = "";


    evaluationMessage.textContent = "";


    nextQuestionBtn.textContent =
        questionNumber >= totalQuestions
            ? "Finish Interview"
            : "Next Question →";


    speakQuestionBtn.disabled =
        false;

}


/* =========================================================
   CLEAN QUESTION
========================================================= */

function cleanQuestion(text) {

    if (!text) {

        return "Please introduce yourself.";

    }


    return text
        .replace(
            /^Interviewer:\s*/i,
            ""
        )
        .trim();

}


/* =========================================================
   QUESTION PROGRESS
========================================================= */

function updateQuestionProgress() {

    questionProgress.innerHTML = "";


    for (
        let i = 1;
        i <= totalQuestions;
        i++
    ) {

        const item =
            document.createElement("span");


        if (
            i < questionNumber
        ) {

            item.classList.add(
                "done"
            );

        } else if (
            i === questionNumber
        ) {

            item.classList.add(
                "current"
            );

        }


        questionProgress.appendChild(
            item
        );

    }

}


/* =========================================================
   SPEAK QUESTION
========================================================= */

function speakQuestion() {

    if (
        !("speechSynthesis" in window)
    ) {

        showRedAlert(
            "Voice Not Available",
            "Your browser does not support text-to-speech.",
            false
        );

        return;
    }


    window.speechSynthesis.cancel();


    const utterance =
        new SpeechSynthesisUtterance(
            cleanQuestion(
                currentQuestion
            )
        );


    utterance.rate = 0.92;

    utterance.pitch = 1;

    utterance.volume = 1;


    window.speechSynthesis.speak(
        utterance
    );

}


/* =========================================================
   VOICE ANSWER
========================================================= */

function startVoiceAnswer() {

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;


    if (!SpeechRecognition) {

        showRedAlert(
            "Voice Input Not Supported",
            "Please use Chrome or Edge for voice answers.",
            false
        );

        return;
    }


    if (voiceListening) {

        if (recognition) {

            try {

                recognition.stop();

            } catch (_) {}

        }

        return;

    }


    recognition =
        new SpeechRecognition();


    recognition.lang =
        "en-IN";


    recognition.continuous =
        true;


    recognition.interimResults =
        true;


    recognition.onstart = () => {

        voiceListening = true;

        voiceAnswerBtn.textContent =
            "🔴 Listening...";

        voiceAnswerBtn.classList.add(
            "recording"
        );

    };


    recognition.onresult = (
        event
    ) => {

        let transcript = "";


        for (
            let i = event.resultIndex;
            i < event.results.length;
            i++
        ) {

            transcript +=
                event.results[i][0]
                    .transcript;

        }


        answerInput.value =
            transcript;

    };


    recognition.onerror = (
        event
    ) => {

        console.warn(
            "Speech recognition:",
            event.error
        );

    };


    recognition.onend = () => {

        voiceListening = false;

        voiceAnswerBtn.textContent =
            "🎤 Speak Answer";

        voiceAnswerBtn.classList.remove(
            "recording"
        );

    };


    try {

        recognition.start();

    } catch (error) {

        console.warn(
            "Recognition start error:",
            error
        );

    }

}


/* =========================================================
   SUBMIT ANSWER
========================================================= */

async function submitAnswer() {

    const answer =
        answerInput.value.trim();


    if (!answer) {

        showRedAlert(
            "Answer Required",
            "Please type or speak your answer first.",
            false
        );

        return;

    }


    nextQuestionBtn.disabled =
        true;

    voiceAnswerBtn.disabled =
        true;


    evaluationMessage.textContent =
        "✦ Skill Up AI is evaluating your answer...";


    history.push({

        role: "user",

        content:
            answer

    });


    try {

        /*
         * Current modular version:
         * /api/interview/next
         */

        const response =
            await fetch(
                "/api/interview/next",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        role: role,

                        level: level,

                        message: answer,

                        history:
                            history,

                        warnings:
                            warningEvents

                    })

                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.error ||
                "Interview request failed."
            );

        }


        /*
         * Last question
         */

        if (
            questionNumber >=
            totalQuestions
        ) {

            await finishInterview(
                data.message || ""
            );

            return;

        }


        questionNumber++;


        const nextQuestion =
            data.message ||
            "Can you explain your approach?";


        history.push({

            role: "assistant",

            content:
                nextQuestion

        });


        displayQuestion(
            nextQuestion
        );


    } catch (error) {

        console.error(
            "Interview request error:",
            error
        );


        /*
         * Compatibility fallback:
         *
         * Some earlier versions of your backend used
         * /api/interview/message.
         */

        try {

            const fallbackResponse =
                await fetch(
                    "/api/interview/message",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify({

                                role: role,

                                level: level,

                                message: answer,

                                history:
                                    history

                            })

                    }
                );


            const fallbackData =
                await fallbackResponse.json();


            if (!fallbackResponse.ok) {

                throw new Error(
                    fallbackData.error ||
                    "Fallback interview request failed."
                );

            }


            if (
                questionNumber >=
                totalQuestions
            ) {

                await finishInterview(
                    fallbackData.message ||
                    ""
                );

                return;

            }


            questionNumber++;


            const nextQuestion =
                fallbackData.message ||
                "Can you explain your approach?";


            history.push({

                role: "assistant",

                content:
                    nextQuestion

            });


            displayQuestion(
                nextQuestion
            );


        } catch (fallbackError) {

            console.error(
                "Fallback error:",
                fallbackError
            );


            evaluationMessage.textContent =
                "Could not contact the AI. Please try again.";

        }

    }


    nextQuestionBtn.disabled =
        false;

    voiceAnswerBtn.disabled =
        false;

}


/* =========================================================
   TAB / WINDOW MONITORING
========================================================= */

function startTabMonitoring() {

    document.addEventListener(
        "visibilitychange",
        handleVisibilityChange
    );


    window.addEventListener(
        "blur",
        handleWindowBlur
    );


    window.addEventListener(
        "focus",
        handleWindowFocus
    );

}


function stopTabMonitoring() {

    document.removeEventListener(
        "visibilitychange",
        handleVisibilityChange
    );


    window.removeEventListener(
        "blur",
        handleWindowBlur
    );


    window.removeEventListener(
        "focus",
        handleWindowFocus
    );

}


/* =========================================================
   TAB SWITCH
========================================================= */

function handleVisibilityChange() {

    if (!interviewStarted) {
        return;
    }


    if (document.hidden) {

        if (!tabWarningActive) {

            tabWarningActive = true;


            tabStatusIcon.textContent =
                "🔴";

            tabStatusText.textContent =
                "Interview tab inactive";


            registerWarning(
                "Tab Switch Detected",
                "You moved away from the interview tab."
            );

        }

    } else {

        tabWarningActive = false;


        tabStatusIcon.textContent =
            "🟢";

        tabStatusText.textContent =
            "Interview window active";

    }

}


/* =========================================================
   WINDOW FOCUS LOST
========================================================= */

function handleWindowBlur() {

    if (!interviewStarted) {
        return;
    }


    /*
     * visibilitychange handles most browser tab switches.
     * blur catches additional cases such as another
     * browser window gaining focus.
     */

    if (
        !document.hidden &&
        !windowWarningActive
    ) {

        windowWarningActive = true;


        tabStatusIcon.textContent =
            "🔴";

        tabStatusText.textContent =
            "Window focus lost";


        registerWarning(
            "Window Focus Lost",
            "Please keep the interview window active."
        );

    }

}


/* =========================================================
   WINDOW FOCUS RETURN
========================================================= */

function handleWindowFocus() {

    if (!interviewStarted) {
        return;
    }


    windowWarningActive = false;


    if (!document.hidden) {

        tabStatusIcon.textContent =
            "🟢";

        tabStatusText.textContent =
            "Interview window active";

    }

}


/* =========================================================
   RED FLAG REGISTRATION
========================================================= */

function registerWarning(
    title,
    message
) {

    warningCount++;


    warningCountElement.textContent =
        warningCount;


    warningEvents.push({

        type:
            title,

        message:
            message,

        timestamp:
            new Date().toISOString()

    });


    showRedAlert(
        title,
        message,
        true
    );


    addWarningToAlertList(
        title
    );

}


/* =========================================================
   ALERT DISPLAY
========================================================= */

function showRedAlert(
    title,
    message,
    isRedFlag
) {

    if (!redAlert) {
        return;
    }


    alertTitle.textContent =
        title;


    alertMessage.textContent =
        message;


    redAlert.classList.remove(
        "hidden"
    );


    if (isRedFlag) {

        redAlert.classList.add(
            "strong-alert"
        );

    } else {

        redAlert.classList.remove(
            "strong-alert"
        );

    }


    clearTimeout(
        alertTimeout
    );


    alertTimeout =
        setTimeout(
            () => {

                redAlert.classList.add(
                    "hidden"
                );

            },
            3500
        );

}


/* =========================================================
   OPTIONAL WARNING LIST SUPPORT
========================================================= */

function addWarningToAlertList(
    title
) {

    /*
     * Your current HTML doesn't require an alert list.
     * This function simply keeps the warning system
     * compatible with earlier interview layouts that
     * used #alertsList.
     */

    const alertsList =
        document.getElementById(
            "alertsList"
        );


    if (!alertsList) {
        return;
    }


    const item =
        document.createElement("p");


    item.className =
        "red-flag-item";


    item.textContent =
        `⚠ ${title}`;


    alertsList.prepend(item);

}


/* =========================================================
   FINISH INTERVIEW
========================================================= */

async function finishInterview(
    finalMessage = ""
) {

    interviewStarted = false;


    stopTabMonitoring();


    stopMedia();


    stopVoiceRecognition();


    stopSpeech();


    try {

        const response =
            await fetch(
                "/api/interview/feedback",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            role: role,

                            level: level,

                            history:
                                history,

                            warnings:
                                warningEvents

                        })

                }
            );


        const data =
            await response.json();


        if (response.ok) {

            resultSummary.textContent =
                "Your interview has been completed. Review your AI feedback below.";


            feedbackContainer.innerHTML =
                `<div class="feedback-text">${
                    data.feedback ||
                    finalMessage ||
                    "Interview completed successfully."
                }</div>`;

        } else {

            throw new Error(
                data.error ||
                "Feedback failed."
            );

        }


    } catch (error) {

        console.warn(
            "Feedback error:",
            error
        );


        resultSummary.textContent =
            "Interview completed. AI feedback could not be loaded.";


        feedbackContainer.innerHTML =
            `<div class="feedback-text">${
                finalMessage ||
                "Interview completed successfully."
            }</div>`;

    }


    finalWarningCount.textContent =
        warningCount;


    resultScreen.classList.remove(
        "hidden"
    );


    /*
     * Exit browser fullscreen after the
     * final result screen is shown.
     */

    await exitInterviewFullscreen();

}


/* =========================================================
   END INTERVIEW EARLY
========================================================= */

async function finishInterviewEarly() {

    const confirmed =
        window.confirm(
            "Are you sure you want to end the interview?"
        );


    if (!confirmed) {
        return;
    }


    await finishInterview(
        "You ended the interview early."
    );

}


/* =========================================================
   STOP MEDIA
========================================================= */

function stopMedia() {

    if (cameraStream) {

        cameraStream
            .getTracks()
            .forEach(
                track => track.stop()
            );

        cameraStream = null;

    }


    if (screenStream) {

        screenStream
            .getTracks()
            .forEach(
                track => track.stop()
            );

        screenStream = null;

    }


    if (cameraVideo) {

        cameraVideo.srcObject =
            null;

    }


    mediaReady.camera =
        false;

    mediaReady.microphone =
        false;

    mediaReady.screen =
        false;

}


/* =========================================================
   STOP VOICE
========================================================= */

function stopVoiceRecognition() {

    if (!recognition) {
        return;
    }


    try {

        recognition.stop();

    } catch (_) {}


    recognition = null;

    voiceListening = false;


    if (voiceAnswerBtn) {

        voiceAnswerBtn.textContent =
            "🎤 Speak Answer";

        voiceAnswerBtn.classList.remove(
            "recording"
        );

    }

}


/* =========================================================
   STOP SPEECH
========================================================= */

function stopSpeech() {

    if (
        "speechSynthesis"
        in window
    ) {

        window.speechSynthesis.cancel();

    }

}


/* =========================================================
   RESTART
========================================================= */

function restartInterview() {

    stopMedia();

    stopTabMonitoring();

    stopVoiceRecognition();

    stopSpeech();


    warningCount = 0;

    warningEvents = [];


    warningCountElement.textContent =
        "0";


    finalWarningCount.textContent =
        "0";


    currentQuestion = "";

    questionNumber = 0;

    history = [];


    resultScreen.classList.add(
        "hidden"
    );


    setupModal.classList.remove(
        "hidden"
    );


    questionText.textContent =
        "Preparing your interview...";


    questionCounter.textContent =
        "QUESTION 0 / 0";


    questionProgress.innerHTML =
        "";


    tabStatusIcon.textContent =
        "🟢";

    tabStatusText.textContent =
        "Interview window active";


    gazeStatusIcon.textContent =
        "🟢";

    gazeStatusText.textContent =
        "Looking at screen";


    updateStartButton();

}


/* =========================================================
   FULLSCREEN CHANGE
========================================================= */

document.addEventListener(
    "fullscreenchange",
    () => {

        if (!document.fullscreenElement) {

            fullscreenRequested =
                false;

            /*
             * Don't create a red flag merely because the
             * browser exited fullscreen. The user may
             * intentionally leave it.
             */

        }

    }
);


/* =========================================================
   BUTTON EVENTS
========================================================= */

if (enableMediaBtn) {

    enableMediaBtn.addEventListener(
        "click",
        enableMedia
    );

}


if (startInterviewBtn) {

    startInterviewBtn.addEventListener(
        "click",
        startInterview
    );

}


if (speakQuestionBtn) {

    speakQuestionBtn.addEventListener(
        "click",
        speakQuestion
    );

}


if (voiceAnswerBtn) {

    voiceAnswerBtn.addEventListener(
        "click",
        startVoiceAnswer
    );

}


if (nextQuestionBtn) {

    nextQuestionBtn.addEventListener(
        "click",
        submitAnswer
    );

}


if (endInterviewBtn) {

    endInterviewBtn.addEventListener(
        "click",
        finishInterviewEarly
    );

}


if (restartInterviewBtn) {

    restartInterviewBtn.addEventListener(
        "click",
        restartInterview
    );

}


/* =========================================================
   INITIAL STATE
========================================================= */

updateStartButton();