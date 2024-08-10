function CalculateButton({ onClick, lists }) {
    if (lists.length === 0) return null;

    return (
        <button onClick={onClick} className="p-2 border rounded-md">
            Calcular escaños
        </button>
    );
}

export default CalculateButton;
