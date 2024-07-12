vim.cmd("setlocal tabstop=2 shiftwidth=2")
lvim.format_on_save.enabled = true
lvim.format_on_save.pattern = {
  "*.lua", "*.py", "*.go", "*.mod", "*.ts", "*.json", "*.js", "*.md", "*.java", "*.toml", "*.yml"
}
lvim.colorscheme = "catppuccin-mocha"
lvim.keys.normal_mode["gy"] = ":BufferLineCycleNext<CR>"
lvim.keys.normal_mode["gt"] = ":BufferLineCyclePrev<CR>"

lvim.plugins = {
  {
    'jghauser/mkdir.nvim'
  },
  {
    'nvimtools/none-ls.nvim',
    opts = function(_, opts)
      local nls = require('null-ls').builtins
      opts.sources = { --override lazyvim's default sources
        nls.code_actions.gitsigns,
        -- go
        nls.code_actions.gomodifytags,
        nls.code_actions.impl,
        nls.formatting.goimports,
        nls.diagnostics.golangci_lint,
        -- ts
        nls.formatting.biome.with({
          filetypes = {
            'javascript',
            'javascriptreact',
            'json',
            'jsonc',
            'typescript',
            'typescriptreact',
            'css',
          },
          args = {
            'check',
            '--write',
            '--unsafe',
            '--formatter-enabled=true',
            '--organize-imports-enabled=true',
            '--skip-errors',
            '--stdin-file-path=$FILENAME',
          },
        }),
        -- other
        nls.formatting.stylua,
        nls.formatting.shfmt.with({
          filetypes = { 'sh', 'zsh' },
        }),
      }
      opts.debug = true
      return opts
    end,
  },
  {
    '0x00-ketsu/autosave.nvim',
    event = { "InsertLeave", "TextChanged" },
    config = function()
      require('autosave').setup {
        enable = true,
        prompt_style = 'stdout',
        prompt_message = function()
          return 'Autosave: saved at ' .. vim.fn.strftime('%H:%M:%S')
        end,
        events = { 'InsertLeave', 'TextChanged' },
        conditions = {
          exists = true,
          modifiable = true,
          filename_is_not = {},
          filetype_is_not = {}
        },
        write_all_buffers = false,
        debounce_delay = 135
      }
    end
  },
  {
    "nacro90/numb.nvim",
    event = "BufRead",
    config = function()
      require("numb").setup {
        show_numbers = true,    -- Enable 'number' for the window while peeking
        show_cursorline = true, -- Enable 'cursorline' for the window while peeking
      }
    end,
  },
  {
    "kevinhwang91/nvim-bqf",
    event = { "BufRead", "BufNew" },
    config = function()
      require("bqf").setup({
        auto_enable = true,
        preview = {
          win_height = 12,
          win_vheight = 12,
          delay_syntax = 80,
          border_chars = { "┃", "┃", "━", "━", "┏", "┓", "┗", "┛", "█" },
        },
        func_map = {
          vsplit = "",
          ptogglemode = "z,",
          stoggleup = "",
        },
        filter = {
          fzf = {
            action_for = { ["ctrl-s"] = "split" },
            extra_opts = { "--bind", "ctrl-o:toggle-all", "--prompt", "> " },
          },
        },
      })
    end,
  },
  {
    'Everblush/nvim',
    as = 'everblush',
    config = function()
      vim.cmd.colorscheme "everblush"
    end
  },
  {
    "nvim-pack/nvim-spectre",
    event = "BufRead",
    config = function()
      require("spectre").setup()
    end,
  },
  {
    "npxbr/glow.nvim",
    config = true,
    cmd = "Glow",
    ft = { "markdown" }
  },
  {
    "lewis6991/gitsigns.nvim",
    dependencies = {
      "nvim-lua/plenary.nvim"
    },
    config = function()
      require('gitsigns').setup(
        current_line_blame == true
      )
    end
  },
  {
    "sitiom/nvim-numbertoggle",
  },
  {
    "mrjones2014/nvim-ts-rainbow",
  },
  {
    "kdheepak/lazygit.nvim",
    dependencies = {
      "nvim-lua/plenary.nvim",
    },
    cmd = {
      "LazyGit",
      "LazyGitConfig",
      "LazyGitCurrentFile",
      "LazyGitFilter",
      "LazyGitFilterCurrentFile",
    },
    keys = {
      { "<leader>lg", "<cmd>LazyGit<cr>", desc = "LazyGit" }
    }
  },
  {
    "ray-x/go.nvim",
    dependencies = {
      "ray-x/guihua.lua",
      "neovim/nvim-lspconfig",
      "nvim-treesitter/nvim-treesitter",
    },
    config = function()
      require("go").setup()
    end,
    event = { "CmdlineEnter" },
    ft = { "go", 'gomod' },
    build = ':lua require("go.install").update_all_sync()'
  },
  {
    "hiphish/rainbow-delimiters.nvim",
    event = "BufReadPost",
    config = function()
      local rainbow_delimiters = require "rainbow-delimiters"

      vim.g.rainbow_delimiters = {
        strategy = {
          [""] = rainbow_delimiters.strategy["global"],
          vim = rainbow_delimiters.strategy["local"],
        },
        query = {
          [""] = "rainbow-delimiters",
          lua = "rainbow-blocks",
        },
        highlight = {
          "RainbowDelimiterRed",
          "RainbowDelimiterYellow",
          "RainbowDelimiterBlue",
          "RainbowDelimiterOrange",
          "RainbowDelimiterGreen",
          "RainbowDelimiterViolet",
          "RainbowDelimiterCyan",
        },
      }
    end,
  },
  {
    "Djancyp/better-comments.nvim",
    config = function()
      require('better-comment').Setup({
        tags = {
          {
            name = "TODO",
            fg = "white",
            bg = "#0a7aca",
            bold = true,
            virtual_text = "",
          },
          {
            name = "FIX",
            fg = "white",
            bg = "#f44747",
            bold = true,
            virtual_text = "This is virtual Text from FIX",
          },
          {
            name = "WARNING",
            fg = "#FFA500",
            bg = "",
            bold = false,
            virtual_text = "This is virtual Text from WARNING",
          },
          {
            name = "ERROR",
            fg = "#f44747",
            bg = "",
            bold = true,
            virtual_text = "",
          }
        }
      })
    end
  },
  {
    'brenoprata10/nvim-highlight-colors',
    config = function()
      require("nvim-highlight-colors").setup {
        render = 'virtual',
        virtual_symbol = '⬤',
        virtual_symbol_prefix = ' ',
        virtual_symbol_suffix = ' ',
        virtual_symbol_position = 'inline',
        enable_hex = true,
        enable_rgb = true,
        enable_hsl = true,
        enable_var_usage = true,
        enable_named_colors = true,
        enable_tailwind = true,
        custom_colors = {
          { label = '%-%-theme%-primary%-color',   color = '#0f1219' },
          { label = '%-%-theme%-secondary%-color', color = '#5a5d64' },
        }
      }
    end
  }
}
