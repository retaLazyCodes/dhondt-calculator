function ClearHistoryButton({ onClick, history }) {
    if (history.length === 0) return null;

    return (
        <button onClick={onClick} className="p-2 border rounded-md">
            Limpiar Historial
        </button>
    );
}

export default ClearHistoryButton;
