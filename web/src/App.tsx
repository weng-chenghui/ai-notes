import { useState, useEffect } from 'react'
import type { Manifest, Document } from './types'

function App() {
  const [manifest, setManifest] = useState<Manifest | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [expandedDocs, setExpandedDocs] = useState<Set<string>>(new Set())
  const [theme, setTheme] = useState<'dark' | 'light'>('light')

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
  }, [theme])

  useEffect(() => {
    fetch('./manifest.json')
      .then(res => {
        if (!res.ok) throw new Error('Manifest not found')
        return res.json()
      })
      .then(data => {
        setManifest(data)
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  const toggleExpand = (dir: string) => {
    setExpandedDocs(prev => {
      const next = new Set(prev)
      if (next.has(dir)) {
        next.delete(dir)
      } else {
        next.add(dir)
      }
      return next
    })
  }

  const toggleTheme = () => {
    setTheme(prev => prev === 'dark' ? 'light' : 'dark')
  }

  const formatDate = (dateStr: string) => {
    return new Date(dateStr).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  const extractDate = (dir: string) => {
    const match = dir.match(/^(\d{4}-\d{2}-\d{2})/)
    return match ? match[1] : null
  }

  return (
    <div className="app">
      <header className="header">
        <div className="header-content">
          <div className="logo">
            <span className="logo-icon">◈</span>
            <h1>AI Notes</h1>
          </div>
          <button className="theme-toggle" onClick={toggleTheme} aria-label="Toggle theme">
            {theme === 'dark' ? '☀' : '☾'}
          </button>
        </div>
        <p className="subtitle">A collection of technical documents and research notes</p>
      </header>

      <main className="main">
        {loading && (
          <div className="loading">
            <div className="loading-spinner" />
            <span>Loading documents...</span>
          </div>
        )}

        {error && (
          <div className="empty-state">
            <span className="empty-icon">∅</span>
            <p>No documents available yet.</p>
            <p className="empty-hint">Documents will appear here once they are compiled.</p>
          </div>
        )}

        {manifest && manifest.documents.length === 0 && (
          <div className="empty-state">
            <span className="empty-icon">∅</span>
            <p>No documents available yet.</p>
            <p className="empty-hint">Documents will appear here once they are compiled.</p>
          </div>
        )}

        {manifest && manifest.documents.length > 0 && (
          <>
            <div className="meta">
              <span>Last updated: {formatDate(manifest.generated)}</span>
              <span className="commit">
                <code>{manifest.commit}</code>
              </span>
            </div>

            <ul className="document-list">
              {manifest.documents.map((doc: Document, index: number) => (
                <li 
                  key={doc.dir} 
                  className="document-item"
                  style={{ animationDelay: `${index * 0.05}s` }}
                >
                  <div 
                    className="document-header"
                    onClick={() => toggleExpand(doc.dir)}
                  >
                    <div className="document-info">
                      <span className={`expand-icon ${expandedDocs.has(doc.dir) ? 'expanded' : ''}`}>
                        ›
                      </span>
                      <div className="document-title-group">
                        <h2 className="document-title">{doc.title}</h2>
                        {extractDate(doc.dir) && (
                          <span className="document-date">{extractDate(doc.dir)}</span>
                        )}
                      </div>
                    </div>
                    <div className="document-files-count">
                      {doc.files.length} {doc.files.length === 1 ? 'file' : 'files'}
                    </div>
                  </div>

                  {expandedDocs.has(doc.dir) && (
                    <div className="document-content">
                      <ul className="file-list">
                        {doc.files.map((file) => (
                          <li key={file.name} className="file-item">
                            <a 
                              href={`./${doc.dir}/${file.name}`}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="file-link"
                            >
                              <span className="file-icon">
                                {file.type === 'pdf' ? '◆' : '◇'}
                              </span>
                              <span className="file-name">{file.name}</span>
                              <span className="file-type">{file.type.toUpperCase()}</span>
                            </a>
                          </li>
                        ))}
                      </ul>

                      {doc.files.filter(f => f.type === 'pdf').length > 0 && (
                        <div className="preview-section">
                          <h3 className="preview-title">Preview</h3>
                          {doc.files.filter(f => f.type === 'pdf').map((file) => (
                            <div key={file.name} className="preview-container">
                              <span className="preview-label">{file.name}</span>
                              <iframe
                                src={`./${doc.dir}/${file.name}`}
                                title={`Preview of ${file.name}`}
                                className="preview-iframe"
                              />
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </li>
              ))}
            </ul>
          </>
        )}
      </main>

      <footer className="footer">
        <p>Built with LaTeX + React • Compiled automatically via GitHub Actions</p>
      </footer>
    </div>
  )
}

export default App
