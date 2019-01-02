# Variables to help determine new naming convention in download string - currently only testing different geosupport versions in linux
# New naming convention example: linux_geo18d_184.zip
$legacyVersions = @('18a', '18b', '18c')
$subVersions = 'a', 'b', 'c', 'd', 'e', 'f'
$BASE_URL = 'https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/'

# DL function modified from https://github.com/ogrisel/python-appveyor-demo/blob/master/appveyor/install.ps1
function Download($filename, $url)
{
    $webclient = New-Object System.Net.WebClient
    $basedir = $pwd.Path + "//"
    $filepath = $basedir + $filename
    if (Test-Path $filename)
    {
        Write-Host "Reusing" $filepath
        return $filepath
    }

    # Download and retry up to 3 times in case of network transient errors.
    Write-Host "Downloading" $filename "from" $url
    $retry_attempts = 2
    for ($i = 0; $i -lt $retry_attempts; $i++) {
        try
        {
            Write-Host "Download attempt" $( $i + 1 )
            $webclient.DownloadFile($url, $filepath)
            break
        }
        Catch [Exception]
        {
            Write-Host "Download Error"
            Start-Sleep 1
        }
    }
    if (Test-Path $filepath)
    {
        Write-Host "File saved at" $filepath
    }
    else
    {
        Write-Host "File not downloaded"
        # Retry once to get the error message if any at the last try
        $webclient.DownloadFile($url, $filepath)
    }
    return $filepath
}

if ($isWindows)
{
    # set download and temp directory names
    if ($env:PYTHON_ARCH -eq '64')
    {

        $LOCALDIR = 'geosupport-install-x64'
        $TARGETDIR = 'C:\Program Files\Geosupport Desktop Edition'
        $FILENAME = "gde64_$( $env:GEO_VERSION ).zip"
        $URL = "$( $BASE_URL )$( $FILENAME )"
    }
    elseif ($env:PYTHON_ARCH -eq '32')
    {
        $LOCALDIR = 'geosupport-install-x86'
        $TARGETDIR = 'C:\Program Files (x86)\Geosupport Desktop Edition'
        $FILENAME = "gde_$( $env:GEO_VERSION ).zip"
        $URL = "$( $BASE_URL )$( $FILENAME )"
    }

    # download
    Write-Host "Downloading $env:PYTHON_ARCH bit Geosupport version $env:GEO_VERSION for Windows..."
    $DOWNLOAD_FILE = Download $FILENAME $URL

    # extract
    Write-Host "Extracting..."
    unzip $FILENAME -d $LOCALDIR

    # delete .zip
    rm $FILENAME

    # silently install Geosupport Desktop
    Write-Host "Installing..."
    Start-Process -Wait -FilePath "$( $LOCALDIR )/setup.exe" -Verb runAs -ArgumentList '/s', '/v"/qn"'

    # set Geosupport Environmental variables
    $env:PATH = "$( $TARGETDIR )\bin;$( $env:PATH )"
    $env:GEOFILES = "$( $TARGETDIR )\fls\"

    Write-Host "Install complete."
}

elseif ($isLinux)
{
    if ($legacyVersions -contains $env:GEO_VERSION)
    {
        $FILENAME = "gdelx_$( $env:GEO_VERSION ).zip"
    }

    # determine string if new geosupport download naming convention
    else
    {
        foreach ($version in $subVersions)
        {
            if ($version -eq $env:GEO_VERSION.Substring(2))
            {
                $idx = [array]::indexOf($subVersions, $version) + 1
                $FILENAME = "linux_geo$( $env:GEO_VERSION )_$($env:GEO_VERSION.Substring(0, 2) )$( $idx ).zip"
            }
        }
    }

    # set download string and local directory names
    $LOCALDIR = 'geosupport-install-lx'
    $URL = "$( $BASE_URL )$( $FILENAME )"

    # download
    Write-Host "Downloading Geosuport version $env:GEO_VERSION for Linux..."
    Download $FILENAME $URL

    # extract
    Write-Host "Extracting..."
    unzip $FILENAME -d $LOCALDIR

    # get the first child directory name of the unzipped geosupport install dir
    $GEO_DIR_CHILD_NAME = Get-ChildItem $LOCALDIR -Recurse | Where-Object { $_.FullName -like "*$( $env:GEO_VERSION )*" } | Select-Object -First 1 | select -expand Name
    $INSTALL_PATH = "$( $pwd )/$( $LOCALDIR )/$( $GEO_DIR_CHILD_NAME )"

    # delete .zip
    rm $FILENAME

    # set Geosupport Environmental variables
    $env:GEOFILES = "$( $INSTALL_PATH )/fls/"
    $env:LD_LIBRARY_PATH = "$( $INSTALL_PATH )/lib/:$( $env:LD_LIBRARY_PATH )"

    Write-Host "Install complete."
}