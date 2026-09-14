from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "healthcare-dataset-stroke-data.csv"
OUTPUT_DIR = ROOT / "docs" / "assets" / "images"

TEAL = "#0f766e"
ORANGE = "#f97316"
BLUE = "#2563eb"
GRAY = "#64748b"
LIGHT_GRAY = "#e2e8f0"
INK = "#0f172a"


def setup_style() -> None:
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        rc={
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": "#cbd5e1",
            "axes.labelcolor": INK,
            "xtick.color": "#334155",
            "ytick.color": "#334155",
            "grid.color": "#e2e8f0",
            "font.family": "DejaVu Sans",
            "axes.titlesize": 17,
            "axes.labelsize": 12,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
        },
    )


def save(fig: plt.Figure, filename: str) -> None:
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=180, bbox_inches="tight")
    plt.close(fig)


def annotate_bars(ax, suffix="", decimals=1) -> None:
    for patch in ax.patches:
        height = patch.get_height()
        if pd.isna(height):
            continue
        ax.annotate(
            f"{height:.{decimals}f}{suffix}",
            (patch.get_x() + patch.get_width() / 2, height),
            ha="center",
            va="bottom",
            fontsize=10,
            color="#334155",
            xytext=(0, 4),
            textcoords="offset points",
        )


def target_balance(df: pd.DataFrame) -> None:
    labels = {0: "Sem AVC", 1: "Com AVC"}
    counts = df["stroke"].map(labels).value_counts().reindex(["Sem AVC", "Com AVC"])
    pct = counts / len(df) * 100

    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    colors = [TEAL, ORANGE]
    bars = ax.barh(counts.index, counts.values, color=colors)
    ax.set_title("Distribuição da variável-alvo", loc="left", weight="bold")
    ax.set_xlabel("Quantidade de pacientes")
    ax.set_ylabel("")
    ax.set_xlim(0, counts.max() * 1.18)

    for bar, value, percent in zip(bars, counts.values, pct.values):
        ax.text(
            value + counts.max() * 0.025,
            bar.get_y() + bar.get_height() / 2,
            f"{value:,.0f} ({percent:.2f}%)".replace(",", "."),
            va="center",
            fontsize=11,
            color=INK,
        )

    sns.despine(left=True, bottom=True)
    save(fig, "target_balance.png")


def data_quality(df: pd.DataFrame) -> None:
    metrics = pd.Series(
        {
            "BMI ausente": df["bmi"].isna().mean() * 100,
            "Smoking Unknown": (df["smoking_status"] == "Unknown").mean() * 100,
            "Gender Other": (df["gender"] == "Other").mean() * 100,
        }
    )

    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    sns.barplot(x=metrics.index, y=metrics.values, hue=metrics.index, ax=ax, palette=[ORANGE, BLUE, GRAY], legend=False)
    ax.set_title("Pontos de atenção na qualidade dos dados", loc="left", weight="bold")
    ax.set_ylabel("Percentual dos registros")
    ax.set_xlabel("")
    ax.set_ylim(0, max(metrics.max() * 1.25, 5))
    annotate_bars(ax, suffix="%", decimals=2)
    sns.despine()
    save(fig, "data_quality.png")


def numeric_distributions(df: pd.DataFrame) -> None:
    columns = [
        ("age", "Idade"),
        ("avg_glucose_level", "Glicose média"),
        ("bmi", "IMC"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))
    for ax, (column, title) in zip(axes, columns):
        sns.histplot(df[column].dropna(), bins=32, kde=True, color=TEAL, ax=ax)
        median = df[column].median()
        ax.axvline(median, color=ORANGE, linestyle="--", linewidth=2)
        ax.set_title(title, weight="bold", fontsize=13)
        ax.set_xlabel(title)
        ax.set_ylabel("Registros")
        ax.text(
            0.98,
            0.88,
            f"Mediana: {median:.1f}",
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=10,
            color=INK,
            bbox={"facecolor": "white", "edgecolor": LIGHT_GRAY, "boxstyle": "round,pad=0.3"},
        )

    fig.suptitle("Distribuições das variáveis numéricas", x=0.03, ha="left", weight="bold")
    save(fig, "numeric_distributions.png")


def age_risk(df: pd.DataFrame) -> None:
    age_groups = pd.cut(
        df["age"],
        bins=[0, 17, 39, 59, 120],
        labels=["0-17", "18-39", "40-59", "60+"],
        include_lowest=True,
    )
    summary = (
        df.assign(age_group=age_groups)
        .groupby("age_group", observed=False)
        .agg(patients=("stroke", "size"), stroke_cases=("stroke", "sum"), stroke_rate=("stroke", "mean"))
        .reset_index()
    )
    summary["stroke_rate"] *= 100

    fig, ax = plt.subplots(figsize=(8.5, 4.7))
    sns.barplot(data=summary, x="age_group", y="stroke_rate", color=ORANGE, ax=ax)
    ax.set_title("Taxa observada de AVC por faixa etária", loc="left", weight="bold")
    ax.set_xlabel("Faixa etária")
    ax.set_ylabel("Taxa de AVC (%)")
    ax.set_ylim(-0.9, summary["stroke_rate"].max() * 1.25)
    annotate_bars(ax, suffix="%", decimals=2)

    for index, row in summary.iterrows():
        ax.text(
            index,
            -0.45,
            f"n={int(row['patients'])}",
            ha="center",
            va="center",
            fontsize=9,
            color="#475569",
        )

    sns.despine()
    save(fig, "age_risk.png")


def clinical_risk(df: pd.DataFrame) -> None:
    rows = []
    for column, label in [("hypertension", "Hipertensão"), ("heart_disease", "Doença cardíaca")]:
        grouped = df.groupby(column)["stroke"].agg(["size", "sum", "mean"]).reset_index()
        for _, row in grouped.iterrows():
            rows.append(
                {
                    "Variavel": label,
                    "Grupo": "Sim" if row[column] == 1 else "Não",
                    "Pacientes": int(row["size"]),
                    "Taxa": row["mean"] * 100,
                }
            )

    summary = pd.DataFrame(rows)
    fig, ax = plt.subplots(figsize=(8.8, 4.7))
    sns.barplot(data=summary, x="Variavel", y="Taxa", hue="Grupo", palette=[TEAL, ORANGE], ax=ax)
    ax.set_title("Taxa observada de AVC por condições clínicas", loc="left", weight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Taxa de AVC (%)")
    ax.set_ylim(0, summary["Taxa"].max() * 1.22)
    ax.legend(title="Grupo", frameon=False)
    annotate_bars(ax, suffix="%", decimals=2)
    sns.despine()
    save(fig, "clinical_risk.png")


def numeric_profile_by_stroke(df: pd.DataFrame) -> None:
    labels = {0: "Sem AVC", 1: "Com AVC"}
    columns = [
        ("age", "Idade média", "anos"),
        ("avg_glucose_level", "Glicose média", "mg/dL"),
        ("bmi", "IMC médio", ""),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))
    for ax, (column, title, unit) in zip(axes, columns):
        summary = (
            df.assign(stroke_label=df["stroke"].map(labels))
            .groupby("stroke_label")[column]
            .mean()
            .reindex(["Sem AVC", "Com AVC"])
            .reset_index()
        )
        sns.barplot(
            data=summary,
            x="stroke_label",
            y=column,
            hue="stroke_label",
            palette=[TEAL, ORANGE],
            legend=False,
            ax=ax,
        )
        ax.set_title(title, weight="bold", fontsize=13)
        ax.set_xlabel("")
        ax.set_ylabel(unit)
        ax.set_ylim(0, summary[column].max() * 1.22)
        annotate_bars(ax, decimals=1)

    fig.suptitle("Perfil numérico médio por classe", x=0.03, ha="left", weight="bold")
    save(fig, "numeric_profile_by_stroke.png")


def categorical_rates(df: pd.DataFrame) -> None:
    columns = [
        ("smoking_status", "Tabagismo"),
        ("work_type", "Tipo de trabalho"),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
    for ax, (column, title) in zip(axes, columns):
        summary = (
            df.groupby(column)["stroke"]
            .agg(patients="size", rate="mean")
            .assign(rate=lambda data: data["rate"] * 100)
            .sort_values("rate", ascending=False)
            .reset_index()
        )
        sns.barplot(data=summary, y=column, x="rate", color=BLUE, ax=ax)
        ax.set_title(title, weight="bold", fontsize=13)
        ax.set_xlabel("Taxa de AVC (%)")
        ax.set_ylabel("")
        ax.set_xlim(0, max(summary["rate"].max() * 1.25, 5))
        for index, row in summary.iterrows():
            ax.text(
                row["rate"] + 0.15,
                index,
                f"{row['rate']:.2f}% | n={int(row['patients'])}",
                va="center",
                fontsize=9,
                color="#334155",
            )

    fig.suptitle("Taxas por variáveis categóricas", x=0.03, ha="left", weight="bold")
    save(fig, "categorical_rates.png")


def correlation_with_target(df: pd.DataFrame) -> None:
    numeric = df[["age", "hypertension", "heart_disease", "avg_glucose_level", "bmi", "stroke"]]
    corr = numeric.corr(numeric_only=True)["stroke"].drop("stroke").sort_values()

    fig, ax = plt.subplots(figsize=(8.5, 4.7))
    colors = [ORANGE if value > 0 else BLUE for value in corr.values]
    ax.barh(corr.index, corr.values, color=colors)
    ax.axvline(0, color="#94a3b8", linewidth=1)
    ax.set_title("Correlação linear com a variável-alvo", loc="left", weight="bold")
    ax.set_xlabel("Correlação de Pearson com stroke")
    ax.set_ylabel("")
    for index, value in enumerate(corr.values):
        ax.text(
            value + 0.01,
            index,
            f"{value:.2f}",
            va="center",
            fontsize=10,
            color=INK,
        )
    sns.despine(left=True)
    save(fig, "target_correlation.png")


def pca_numeric(df: pd.DataFrame) -> None:
    numeric = df[["age", "avg_glucose_level", "bmi", "stroke"]].dropna()
    features = numeric[["age", "avg_glucose_level", "bmi"]]
    scaled = StandardScaler().fit_transform(features)
    pca = PCA(n_components=2, random_state=42)
    components = pca.fit_transform(scaled)

    plot_df = pd.DataFrame(components, columns=["PC1", "PC2"])
    plot_df["stroke"] = numeric["stroke"].map({0: "Sem AVC", 1: "Com AVC"}).values

    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    sns.scatterplot(
        data=plot_df,
        x="PC1",
        y="PC2",
        hue="stroke",
        hue_order=["Sem AVC", "Com AVC"],
        palette=[GRAY, ORANGE],
        alpha=0.45,
        s=28,
        edgecolor=None,
        ax=ax,
    )
    explained = pca.explained_variance_ratio_ * 100
    ax.set_title("PCA das variáveis numéricas", loc="left", weight="bold")
    ax.set_xlabel(f"PC1 ({explained[0]:.1f}% da variância)")
    ax.set_ylabel(f"PC2 ({explained[1]:.1f}% da variância)")
    ax.legend(title="Classe", frameon=False)
    sns.despine()
    save(fig, "pca_numeric.png")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    setup_style()
    df = pd.read_csv(DATASET, na_values=["N/A"])

    target_balance(df)
    data_quality(df)
    numeric_distributions(df)
    age_risk(df)
    clinical_risk(df)
    numeric_profile_by_stroke(df)
    categorical_rates(df)
    correlation_with_target(df)
    pca_numeric(df)


if __name__ == "__main__":
    main()
