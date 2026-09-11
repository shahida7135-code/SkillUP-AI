let conversation = [];


const input =
    document.getElementById(
        "messageInput"
    );


const sendButton =
    document.getElementById(
        "sendButton"
    );


const chatMessages =
    document.getElementById(
        "chatMessages"
    );



input.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter"
        ) {

            sendMessage();

        }

    }
);



function escapeHTML(text) {

    const element =
        document.createElement("div");

    element.textContent =
        text;

    return element.innerHTML;

}



function addMessage(
    text,
    sender
) {

    const row =
        document.createElement("div");


    row.className =
        "chat-row " + sender;


    if (
        sender === "assistant"
    ) {

        row.innerHTML =
            `
            <div class="chat-avatar">
                S
            </div>

            <div class="chat-bubble">
                ${escapeHTML(text)}
            </div>
            `;

    } else {

        row.innerHTML =
            `
            <div class="chat-bubble">
                ${escapeHTML(text)}
            </div>
            `;

    }


    chatMessages.appendChild(
        row
    );


    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}



function addTyping() {

    const row =
        document.createElement("div");


    row.id =
        "typingIndicator";


    row.className =
        "chat-row assistant";


    row.innerHTML =
        `
        <div class="chat-avatar">
            S
        </div>

        <div class="chat-bubble typing">
            Thinking...
        </div>
        `;


    chatMessages.appendChild(row);


    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}



function removeTyping() {

    const typing =
        document.getElementById(
            "typingIndicator"
        );


    if (typing) {

        typing.remove();

    }

}



async function sendMessage() {

    const text =
        input.value.trim();


    if (!text) {

        return;

    }


    addMessage(
        text,
        "user"
    );


    conversation.push({

        role: "user",

        content: text

    });


    input.value = "";

    sendButton.disabled = true;

    addTyping();


    try {

        const response =
            await fetch(
                "/api/tutor",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            message:
                                text,

                            history:
                                conversation

                        })
                }
            );


        const data =
            await response.json();


        removeTyping();


        if (!response.ok) {

            throw new Error(
                data.error ||
                "AI request failed."
            );

        }


        addMessage(
            data.answer,
            "assistant"
        );


        conversation.push({

            role: "assistant",

            content: data.answer

        });


    } catch (error) {

        removeTyping();


        addMessage(
            "Sorry, I couldn't connect to the AI right now.",
            "assistant"
        );


        console.error(error);

    }


    sendButton.disabled = false;

    input.focus();

}



function quickAsk(question) {

    input.value =
        question;

    sendMessage();

}