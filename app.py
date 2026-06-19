import time

import streamlit as st

from game_logic import check_winner, create_board, is_draw, make_move
from minimax import best_move


st.set_page_config(
    page_title="Tic-Tac-Toe AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)


def initialize_game():
    st.session_state.board = create_board()
    st.session_state.game_over = False
    st.session_state.ai_pending = False
    st.session_state.ai_pending_started_at = None
    st.session_state.status_message = "Your Turn (X)"
    st.session_state.result_message = ""
    st.session_state.result_type = "info"


def restart_game():
    initialize_game()
    st.rerun()


def finish_game(message, result_type):
    st.session_state.game_over = True
    st.session_state.ai_pending = False
    st.session_state.ai_pending_started_at = None
    st.session_state.status_message = message
    st.session_state.result_message = message
    st.session_state.result_type = result_type


def play_ai_turn():
    if st.session_state.game_over:
        return

    move = best_move(st.session_state.board)
    if move is None:
        if is_draw(st.session_state.board):
            finish_game("The game ended in a draw.", "info")
        return

    make_move(st.session_state.board, move, "O")

    winner = check_winner(st.session_state.board)
    if winner == "O":
        finish_game("AI Won!", "error")
    elif is_draw(st.session_state.board):
        finish_game("It's a Draw!", "info")
    else:
        st.session_state.ai_pending = False
        st.session_state.ai_pending_started_at = None
        st.session_state.status_message = "AI Played O - Your Turn (X)"


def queue_ai_turn():
    st.session_state.ai_pending = True
    st.session_state.ai_pending_started_at = time.time()
    st.session_state.status_message = "🤖 AI is thinking..."


def handle_human_move(index):
    if st.session_state.game_over or st.session_state.ai_pending:
        return
    if not make_move(st.session_state.board, index, "X"):
        return

    winner = check_winner(st.session_state.board)
    if winner == "X":
        finish_game("You Won!", "success")
        return

    if is_draw(st.session_state.board):
        finish_game("It's a Draw!", "info")
        return

    queue_ai_turn()


if "board" not in st.session_state:
    initialize_game()


st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at top, rgba(120, 120, 120, 0.12), transparent 35%),
                linear-gradient(180deg, #080808 0%, #141414 100%);
            color: #ffffff;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 820px;
        }
        h1, h2, h3, p, div, span {
            color: #ffffff;
        }
        h1 {
            font-size: 3rem;
            line-height: 1.1;
            margin-bottom: 0.25rem;
        }
        .hero-copy {
            color: #cfcfcf;
            font-size: 1rem;
            margin-bottom: 1rem;
        }
        .badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin: 1rem 0 1.1rem;
        }
        .badge {
            background: #1f1f1f;
            border: 1px solid #343434;
            border-radius: 999px;
            padding: 0.45rem 0.8rem;
            color: #f0f0f0;
            font-size: 0.88rem;
            letter-spacing: 0.01em;
        }
        .game-card {
            background: linear-gradient(180deg, #1a1a1a 0%, #121212 100%);
            border: 1px solid #2d2d2d;
            border-radius: 22px;
            padding: 1.35rem;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.42);
        }
        .section-label {
            color: #eaeaea;
            font-size: 0.85rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            margin: 0.9rem 0 0.65rem;
        }
        .status-box {
            background: linear-gradient(180deg, #171717 0%, #111111 100%);
            border: 1px solid #343434;
            border-radius: 14px;
            padding: 0.95rem 1rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }
        .stButton > button {
            background: linear-gradient(180deg, #777777 0%, #5f5f5f 100%);
            color: #ffffff;
            border: 1px solid #949494;
            border-radius: 16px;
            height: 104px;
            font-size: 2.4rem;
            font-weight: 700;
            transition: transform 0.15s ease, background 0.15s ease, box-shadow 0.15s ease;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }
        .stButton > button:hover {
            background: linear-gradient(180deg, #878787 0%, #6a6a6a 100%);
            transform: translateY(-1px);
            box-shadow: 0 8px 18px rgba(0, 0, 0, 0.2);
        }
        .stButton > button:disabled {
            background: #2a2a2a;
            color: #f4f4f4;
            border-color: #404040;
            opacity: 1;
        }
        .stButton > button[kind="primary"] {
            background: linear-gradient(180deg, #ff6b6b 0%, #d64545 100%);
            color: #ffffff;
            border-color: #ff8a8a;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.12);
        }
        .stButton > button[kind="primary"]:hover {
            background: linear-gradient(180deg, #ff7c7c 0%, #c93b3b 100%);
        }
        .stAlert {
            border-radius: 12px;
        }
        .stButton p{
            font-size: 26px;
            font-weight: 700;
        }
        .thinking-card {
            background: linear-gradient(180deg, #171717 0%, #101010 100%);
            border: 1px solid #3d3d3d;
            border-radius: 16px;
            padding: 0.75rem 0.8rem;
            min-height: 92px;
            display: flex;
            align-items: center;
        }
        .thinking-title {
            font-size: 0.72rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #d7d7d7;
            margin-bottom: 0.3rem;
        }
        .thinking-text {
            font-size: 0.92rem;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .thinking-dot {
            display: inline-block;
            width: 0.7rem;
            height: 0.7rem;
            border-radius: 50%;
            background: #ff6b6b;
            box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.5);
            animation: pulse 1.1s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.45); }
            70% { transform: scale(1); box-shadow: 0 0 0 12px rgba(255, 107, 107, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 107, 107, 0); }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🤖 Tic-Tac-Toe AI")
st.markdown(
    '<div class="hero-copy">Human plays as X, AI plays as O. The AI uses Minimax and always picks the optimal response.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="badge-row">
        <div class="badge">Unbeatable Minimax AI</div>
        <div class="badge">3×3 Classic Board</div>
        <div class="badge">Clean Streamlit UI</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="status-box"><span><strong>Current Status:</strong> {st.session_state.status_message}</span><span>Human: X | AI: O</span></div>',
    unsafe_allow_html=True,
)

if st.session_state.result_message:
    if st.session_state.result_type == "success":
        st.success(st.session_state.result_message)
    elif st.session_state.result_type == "error":
        st.error(st.session_state.result_message)
    else:
        st.info(st.session_state.result_message)

ai_turn_pending = st.session_state.ai_pending and not st.session_state.game_over

board_column, thinking_column = st.columns([3, 1], gap="medium")

with board_column:
    st.markdown('<div class="section-label">Game Board</div>', unsafe_allow_html=True)

    for row in range(3):
        columns = st.columns(3, gap="small")
        for column_index, column in enumerate(columns):
            cell_index = row * 3 + column_index
            cell_value = st.session_state.board[cell_index] or " "
            disabled = st.session_state.game_over or st.session_state.ai_pending or st.session_state.board[cell_index] != ""
            with column:
                st.button(
                    cell_value,
                    key=f"cell_{cell_index}",
                    use_container_width=True,
                    disabled=disabled,
                    on_click=handle_human_move,
                    args=(cell_index,),
                )

with thinking_column:
    if ai_turn_pending:
        st.markdown(
            """
            <div class="thinking-card">
                <div>
                    <div class="thinking-title">AI Status</div>
                    <div class="thinking-text"><span class="thinking-dot"></span>🤖 AI is thinking...</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="thinking-card">
                <div>
                    <div class="thinking-title">AI Status</div>
                    <div class="thinking-text">Ready for your move.</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

left, right = st.columns([3.75, 1.25])

with left:
    st.button("Restart Game", type="primary", use_container_width=True, on_click=restart_game)

if ai_turn_pending:
    elapsed = time.time() - st.session_state.ai_pending_started_at if st.session_state.ai_pending_started_at else 0
    remaining_delay = max(0.55 - elapsed, 0)
    if remaining_delay:
        time.sleep(remaining_delay)

    play_ai_turn()
    st.rerun()
