local options = {
  formatters_by_ft = {
    lua = { "stylua" },
    go = { "golines" },
    python = { "ruff" },
    javascript = { "biome" },
    typescript = { "biome" },
  },

  format_on_save = {
    timeout_ms = 500,
    lsp_fallback = true,
  },
}

require("conform").setup(options)
